#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TỰ ĐỘNG ĐỒNG BỘ 2 CHIỀU VỚI GITHUB (AUTO-SYNC ENGINE) — AI-DRIVEN DOCUMENTARY FACTORY
"""
import subprocess, sys, datetime
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

def sync_to_github(commit_msg: str = ""):
    script_path = Path(__file__).resolve()
    repo_root = None
    for p in list(script_path.parents) + [Path.cwd().resolve()] + list(Path.cwd().resolve().parents):
        if (p / ".git").exists():
            repo_root = p
            break
    if not repo_root:
        print("[Auto-Sync] Không tìm thấy kho .git")
        return False

    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if not commit_msg:
        commit_msg = f"chore(auto-sync): cập nhật tự động lúc {now_str}"

    try:
        st = subprocess.run(["git", "status", "--porcelain"], cwd=str(repo_root), capture_output=True, text=True)
        if st.stdout.strip():
            subprocess.run(["git", "add", "-A"], cwd=str(repo_root), check=False)
            subprocess.run(["git", "commit", "-m", commit_msg], cwd=str(repo_root), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        subprocess.run(["git", "pull", "--rebase", "origin", "main"], cwd=str(repo_root), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        push_res = subprocess.run(["git", "push", "origin", "main", "--tags"], cwd=str(repo_root), capture_output=True, text=True)
        if push_res.returncode == 0:
            print(f"[Auto-Sync GitHub OK] Đã đồng bộ lên GitHub ({now_str})")
            return True
        else:
            print(f"[Auto-Sync GitHub WARN] Lỗi khi push: {push_res.stderr.strip()}")
            return False
    except Exception as e:
        print(f"[Auto-Sync GitHub WARN] Ngoại lệ: {e}")
        return False

if __name__ == "__main__":
    msg = " ".join(sys.argv[1:]).strip()
    sync_to_github(msg)
