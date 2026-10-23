"""
PHA 3: CÔNG CỤ SĂN NGUYÊN LIỆU ĐA NGUỒN & LƯU ĐÚNG MÃ STT (CHỐNG LƯU BỪA)
- Chỉ chạy sau khi người dùng đã duyệt Bảng Đạo Diễn ở Pha 2.
- Mọi file tải về bắt buộc đặt tên gắn cứng với mã `stt_id` ở Pha 2:
    Ví dụ: 01_00m00s_polaroid_alaska_check.jpg
           02_00m09s_sticker_tsar_alexander.png
           03_00m17s_video_bering_strait.mp4
- Nếu không tìm thấy ở nguồn số 1, tự động tìm phương án thay thế ở nguồn 2, 3 (_alt2, _alt3)
  và ghi rõ vào báo cáo `asset_verification_report.json` để AI kiểm duyệt bằng mắt (`read_file`).
"""
import os
import sys
import io

_PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
if os.path.isdir(_PROJECT_ROOT) and os.path.exists(os.path.join(_PROJECT_ROOT, "index.html")):
    os.chdir(_PROJECT_ROOT)
import json
import urllib.request
import urllib.parse
import re
import subprocess
import imageio_ffmpeg
from PIL import Image, ImageOps, ImageEnhance, ImageFilter

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

HEADERS = {
    "User-Agent": "SuDeHieuDocumentaryBot/1.0 (https://sudehieu.vn; contact@sudehieu.vn) Python/3.12"
}
FFMPEG_EXE = imageio_ffmpeg.get_ffmpeg_exe()

BANNED_FILENAME_WORDS = [
    "flag_of", "coat_of_arms", "locator_map", "location_map", "icon",
    "logo", "symbol", "stub", "signature", "autograph", "plaque", "memorial_stone",
    "commons-logo", "speakerlink", "padlock"
]


def is_valid_image_url(url):
    clean_u = url.split("?")[0].lower()
    filename = clean_u.split("/")[-1]
    if any(clean_u.endswith(ext) for ext in (".svg", ".pdf", ".djvu", ".tif", ".gif", ".ogg", ".webm", ".webp")):
        return False
    for bad in BANNED_FILENAME_WORDS:
        if bad in filename:
            return False
    return True


def search_wikipedia_exact_titles(titles, max_candidates=3):
    candidates = []
    for title in titles:
        if len(candidates) >= max_candidates:
            break
        encoded = urllib.parse.quote(title)
        api_url = (
            f"https://en.wikipedia.org/w/api.php?action=query"
            f"&titles={encoded}&redirects=1"
            f"&prop=pageimages|extracts&piprop=original|thumbnail&pithumbsize=1280"
            f"&exintro=1&explaintext=1&exchars=220&format=json"
        )
        try:
            req = urllib.request.Request(api_url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=8) as r:
                data = json.loads(r.read().decode("utf-8"))
            pages = data.get("query", {}).get("pages", {})
            for p in pages.values():
                orig = p.get("original", {}).get("source")
                thumb = p.get("thumbnail", {}).get("source")
                img_url = thumb or orig
                if img_url and is_valid_image_url(img_url):
                    candidates.append({
                        "url": img_url,
                        "verified_title": p.get("title", title),
                        "historical_context": (p.get("extract") or "").replace("\n", " ").strip()[:180],
                        "source": f"Wikipedia ({p.get('title', title)})"
                    })
        except Exception:
            pass
    return candidates


def search_wikimedia_commons_files(query, max_candidates=3):
    candidates = []
    encoded = urllib.parse.quote(query)
    api_url = (
        f"https://commons.wikimedia.org/w/api.php?action=query"
        f"&generator=search&gsrsearch={encoded}&gsrnamespace=6&gsrlimit=8"
        f"&prop=imageinfo&iiprop=url|extmetadata&iiurlwidth=1280&format=json"
    )
    try:
        req = urllib.request.Request(api_url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=8) as r:
            data = json.loads(r.read().decode("utf-8"))
        pages = data.get("query", {}).get("pages", {})
        sorted_pages = sorted(pages.values(), key=lambda x: x.get("index", 999))
        for p in sorted_pages:
            ii_list = p.get("imageinfo", [])
            if not ii_list:
                continue
            ii = ii_list[0]
            img_url = ii.get("thumburl") or ii.get("url")
            if not img_url or not is_valid_image_url(img_url):
                continue
            title_clean = p.get("title", "").replace("File:", "")
            ext_meta = ii.get("extmetadata", {})
            desc = ext_meta.get("ImageDescription", {}).get("value", "")
            desc_clean = re.sub(r"<[^>]+>", "", desc).strip()[:180]
            candidates.append({
                "url": img_url,
                "verified_title": title_clean,
                "historical_context": desc_clean or title_clean,
                "source": "Wikimedia Commons"
            })
            if len(candidates) >= max_candidates:
                break
    except Exception:
        pass
    return candidates


def fetch_youtube_clip_3_5s(search_query, out_mp4_path, start_sec=10, duration_sec=4.0, wiki_fallback_titles=None):
    print(f"  [YouTube Footage] Đang tìm & cắt {duration_sec}s video cho: '{search_query}'...")
    temp_video = out_mp4_path + ".temp.mp4"
    try:
        cmd_yt = [
            "yt-dlp",
            f"ytsearch3:{search_query}",
            "--ffmpeg-location", FFMPEG_EXE,
            "-f", "b[ext=mp4]/b",
            "--max-downloads", "1",
            "-o", temp_video,
            "--no-playlist", "--quiet", "--no-warnings"
        ]
        subprocess.run(cmd_yt, timeout=45, check=False)

        if os.path.exists(temp_video):
            cmd_ff = [
                FFMPEG_EXE, "-y",
                "-ss", str(start_sec),
                "-i", temp_video,
                "-t", str(duration_sec),
                "-vf", "scale=960:540:force_original_aspect_ratio=increase,crop=960:540,hue=s=0,eq=contrast=1.15:brightness=-0.03",
                "-an",
                "-c:v", "libx264", "-preset", "ultrafast", "-crf", "23", "-pix_fmt", "yuv420p",
                out_mp4_path
            ]
            subprocess.run(cmd_ff, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=30)
            try:
                os.remove(temp_video)
            except Exception:
                pass
            if os.path.exists(out_mp4_path):
                print(f"  + Đã lưu đúng STT -> {os.path.basename(out_mp4_path)}")
                return True, "YouTube Archival Footage"
    except Exception as e:
        print(f"  ! Cảnh báo cắt video: {e}")
    finally:
        if os.path.exists(temp_video):
            try:
                os.remove(temp_video)
            except Exception:
                pass

    # Phương án thay thế tự động: Tạo đoạn băng chuyển động 4s (Archival Ken Burns Motion Clip) từ tư liệu Wikimedia Commons
    print(f"  [Phương án Thay thế Video] Đang tạo đoạn băng tư liệu chuyển động 4.0s từ Wikimedia Commons...")
    cands = search_wikimedia_commons_files(search_query, max_candidates=2)
    if not cands and wiki_fallback_titles:
        cands = search_wikipedia_exact_titles(wiki_fallback_titles, max_candidates=2)
    if cands:
        try:
            req = urllib.request.Request(cands[0]["url"], headers=HEADERS)
            img_bytes = urllib.request.urlopen(req, timeout=10).read()
            im = to_archival_bw(Image.open(io.BytesIO(img_bytes))).resize((1280, 720), Image.Resampling.LANCZOS)
            tmp_jpg = out_mp4_path + ".still.jpg"
            im.save(tmp_jpg, quality=92)
            cmd_kb = [
                FFMPEG_EXE, "-y",
                "-loop", "1", "-i", tmp_jpg,
                "-vf", "zoompan=z='min(zoom+0.002,1.25)':d=120:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=960x540:fps=30",
                "-t", str(duration_sec),
                "-c:v", "libx264", "-preset", "ultrafast", "-crf", "22", "-pix_fmt", "yuv420p",
                out_mp4_path
            ]
            subprocess.run(cmd_kb, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=30)
            if os.path.exists(tmp_jpg):
                os.remove(tmp_jpg)
            if os.path.exists(out_mp4_path):
                print(f"  + Đã tạo Video Thay thế 4.0s ({cands[0]['source']}) -> {os.path.basename(out_mp4_path)}")
                return True, f"Phương án Thay thế: Archival Motion Clip ({cands[0]['verified_title'][:40]})"
        except Exception as e:
            print(f"  ! Lỗi tạo video thay thế: {e}")

    return False, "N/A"


def to_archival_bw(img):
    gray = ImageOps.grayscale(img)
    gray = ImageEnhance.Contrast(gray).enhance(1.18)
    return ImageOps.colorize(gray, black="#161412", white="#F6F1E5")


def reframe_to_landscape(bw_img, target_w=1280, target_h=820):
    """Đóng khung ngang an toàn (Safe Archival Matting) cho các bức ảnh dọc/vuông để không bao giờ bị cắt cụt đầu."""
    w, h = bw_img.size
    if w / float(max(1, h)) >= 1.32:
        return ImageOps.fit(bw_img, (target_w, target_h), method=Image.Resampling.LANCZOS, centering=(0.5, 0.35))
    bg = ImageOps.fit(bw_img, (target_w, target_h), method=Image.Resampling.LANCZOS)
    bg = bg.filter(ImageFilter.GaussianBlur(radius=24))
    bg = ImageEnhance.Brightness(bg).enhance(0.45)
    fg = bw_img.copy()
    fg.thumbnail((int(target_w * 0.88), int(target_h * 0.94)), Image.Resampling.LANCZOS)
    ox = (target_w - fg.width) // 2
    oy = (target_h - fg.height) // 2
    bg.paste(fg, (ox, oy))
    return bg


def clean_largest_alpha_component(rgba_img):
    """Loại bỏ các mảnh rác đen/trắng rời rạc ở góc ảnh sau khi tách nền rembg."""
    try:
        import numpy as np
        from scipy import ndimage
        arr = np.array(rgba_img)
        mask = arr[:, :, 3] > 15
        labeled, num = ndimage.label(mask)
        if num > 1:
            sizes = ndimage.sum(mask, labeled, range(1, num + 1))
            largest = int(np.argmax(sizes)) + 1
            keep = (labeled == largest)
            arr[~keep, 3] = 0
            return Image.fromarray(arr)
    except Exception:
        pass
    return rgba_img


def add_white_sticker_border(rgba_img, border_size=10):
    rgba_img = clean_largest_alpha_component(rgba_img)
    alpha = rgba_img.split()[3]
    expanded = alpha.filter(ImageFilter.MaxFilter(border_size * 2 + 1))
    outline = Image.new("RGBA", rgba_img.size, (250, 246, 238, 255))
    outline.putalpha(expanded)
    outline.paste(rgba_img, (0, 0), rgba_img)
    return outline


def extract_media_items_from_blueprint(data):
    """Hỗ trợ đọc cả danh sách phẳng (manifest.json) lẫn File Chỉ Đạo Phân Cảnh Hợp Nhất (chi_dao_phan_canh.json / storyboard.json)."""
    if isinstance(data, list):
        return data, False
    items = []
    for sc in data.get("scenes", []):
        for beat in sc.get("beats", []):
            btype = beat.get("type", "").upper()
            if btype in ("POLAROID", "STICKER", "VIDEO_CLIP", "VIDEO"):
                items.append({
                    "stt_id": beat.get("stt_id"),
                    "type": btype.lower(),
                    "search_query": beat.get("search_query") or beat.get("caption") or beat.get("label") or beat.get("stt_id"),
                    "wiki_titles": beat.get("wiki_titles", []),
                    "expected_subject": beat.get("expected_subject") or beat.get("caption") or beat.get("label") or "",
                    "time_range": f"{beat.get('t0', 0)}s - {beat.get('t1', 0)}s",
                    "clip_start_sec": beat.get("clip_start_sec", 10),
                    "clip_duration_sec": beat.get("clip_duration_sec", 4.0),
                    "_beat_ref": beat
                })
    return items, True


def harvest_assets_by_stt(manifest_path, part_asset_dir):
    dir_polaroid = os.path.join(part_asset_dir, "images_polaroid")
    dir_sticker = os.path.join(part_asset_dir, "stickers_cutout")
    dir_footage = os.path.join(part_asset_dir, "video_footage")
    for d in (dir_polaroid, dir_sticker, dir_footage):
        os.makedirs(d, exist_ok=True)

    with open(manifest_path, encoding="utf-8") as f:
        raw_data = json.load(f)

    items, is_unified_blueprint = extract_media_items_from_blueprint(raw_data)

    try:
        from rembg import remove as rembg_remove
        has_rembg = True
    except Exception:
        has_rembg = False

    report = []
    print("=" * 78)
    print(f"[PHA 3] SĂN NGUYÊN LIỆU & LƯU ĐÚNG MÃ STT ({len(items)} MỤC)")
    print("=" * 78)

    for idx_item, item in enumerate(items, start=1):
        stt_id = item.get("stt_id") or item.get("id") or f"{idx_item:02d}_asset"
        query = item["search_query"]
        wiki_titles = item.get("wiki_titles", [])
        asset_type = item.get("type", "polaroid").lower()
        expected_subject = item.get("expected_subject", query)
        time_range = item.get("time_range", "")

        print(f"\n[{stt_id}] ({asset_type.upper()} | {time_range}) <- '{query}'")

        if asset_type in ("video_clip", "video"):
            out_mp4 = os.path.join(dir_footage, f"{stt_id}.mp4")
            start_s = item.get("clip_start_sec", 10)
            dur_s = item.get("clip_duration_sec", 4.0)
            ok, vid_src = fetch_youtube_clip_3_5s(
                query, out_mp4, start_sec=start_s, duration_sec=dur_s,
                wiki_fallback_titles=wiki_titles or ["Alaska", "Klondike Gold Rush"]
            )
            if ok and "_beat_ref" in item:
                rel_mp4 = out_mp4.replace("\\", "/")
                if "2_KHO_NGUYEN_LIEU/" in rel_mp4:
                    rel_mp4 = "2_KHO_NGUYEN_LIEU/" + rel_mp4.split("2_KHO_NGUYEN_LIEU/", 1)[1]
                item["_beat_ref"]["src"] = rel_mp4
                item["_beat_ref"]["source_origin"] = vid_src
            report.append({
                "stt_id": stt_id,
                "time_range": time_range,
                "type": "video_clip",
                "expected_subject": expected_subject,
                "selected_path": out_mp4.replace("\\", "/") if ok else None,
                "status": f"CÓ ({vid_src})" if ok else "KHÔNG TÌM THẤY (CẦN PHƯƠNG ÁN THAY THẾ)",
                "source": vid_src
            })
            continue

        candidates = []
        if wiki_titles:
            candidates.extend(search_wikipedia_exact_titles(wiki_titles, max_candidates=2))
        if len(candidates) < 4:
            commons_cands = search_wikimedia_commons_files(query, max_candidates=5 - len(candidates))
            for cc in commons_cands:
                if all(cc["url"] != existing["url"] for existing in candidates):
                    candidates.append(cc)

        saved_candidates = []
        target_subdir = dir_sticker if asset_type == "sticker" else dir_polaroid

        for idx, cand in enumerate(candidates[:3]):
            suffix = "" if idx == 0 else f"_alt{idx+1}"
            try:
                req = urllib.request.Request(cand["url"], headers=HEADERS)
                with urllib.request.urlopen(req, timeout=10) as resp:
                    img_bytes = resp.read()

                raw_img = Image.open(io.BytesIO(img_bytes))
                raw_img.load()
                if raw_img.width < 180 or raw_img.height < 180:
                    continue

                raw_img.thumbnail((1280, 1280), Image.Resampling.LANCZOS)
                bw_img = to_archival_bw(raw_img)

                if asset_type == "sticker" and has_rembg:
                    rgba_cutout = rembg_remove(bw_img.convert("RGBA"))
                    sticker_img = add_white_sticker_border(rgba_cutout, border_size=10)
                    final_path = os.path.join(target_subdir, f"{stt_id}{suffix}.png")
                    sticker_img.save(final_path)
                else:
                    framed_img = reframe_to_landscape(bw_img)
                    final_path = os.path.join(target_subdir, f"{stt_id}{suffix}.jpg")
                    framed_img.save(final_path, quality=92)

                rel_final = final_path.replace("\\", "/")
                if "2_KHO_NGUYEN_LIEU/" in rel_final:
                    rel_final = "2_KHO_NGUYEN_LIEU/" + rel_final.split("2_KHO_NGUYEN_LIEU/", 1)[1]

                saved_candidates.append({
                    "option": idx + 1,
                    "local_path": rel_final,
                    "verified_title": cand["verified_title"],
                    "historical_context": cand["historical_context"],
                    "source": cand["source"],
                    "source_url": cand["url"]
                })
                print(f"  + Phương án {idx+1} ({cand['source']}): [{cand['verified_title'][:50]}] -> {os.path.basename(final_path)}")
            except Exception as e:
                print(f"  ! Bỏ qua ứng viên lỗi: {e}")

        if saved_candidates and "_beat_ref" in item:
            item["_beat_ref"]["src"] = saved_candidates[0]["local_path"]
            item["_beat_ref"]["source_origin"] = f"{saved_candidates[0]['source']}: {saved_candidates[0]['verified_title']}"

        report.append({
            "stt_id": stt_id,
            "time_range": time_range,
            "type": asset_type,
            "expected_subject": expected_subject,
            "selected_path": saved_candidates[0]["local_path"] if saved_candidates else None,
            "status": f"CÓ ({saved_candidates[0]['source']})" if saved_candidates else "KHÔNG TÌM THẤY (CẦN PHƯƠNG ÁN THAY THẾ)",
            "candidates": saved_candidates
        })

    if is_unified_blueprint:
        with open(manifest_path, "w", encoding="utf-8") as f:
            json.dump(raw_data, f, ensure_ascii=False, indent=2)
        sb_sync_path = os.path.join(part_asset_dir, "storyboard.json")
        with open(sb_sync_path, "w", encoding="utf-8") as f:
            json.dump(raw_data, f, ensure_ascii=False, indent=2)

    report_path = os.path.join(part_asset_dir, "asset_verification_report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print("\n" + "=" * 78)
    print(f"[HOÀN TẤT PHA 3] Hồ sơ xác thực theo STT đã lưu tại: {report_path}")
    print("🛑 [CỔNG DỪNG 3]: AI bắt buộc mở xem từng ảnh bằng `read_file` và báo cáo chờ duyệt!")
    print("=" * 78)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Cách dùng: python pha-3-san-nguyen-lieu-theo-stt.py <manifest_json> <part_asset_dir>")
        sys.exit(1)
    harvest_assets_by_stt(sys.argv[1], sys.argv[2])
