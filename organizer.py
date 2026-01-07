import os
import shutil
from config import BASE_DIR, RULES
from datetime import datetime

# exe / py 공통 로그 경로 처리
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
LOG_PATH = os.path.join(BASE_PATH, "logs", "history.log")


def get_folder(ext):
    for folder, exts in RULES.items():
        if ext in exts:
            return folder
    return "Others"


def get_unique_path(folder_path, filename):
    name, ext = os.path.splitext(filename)
    candidate = os.path.join(folder_path, filename)
    count = 1

    while os.path.exists(candidate):
        candidate = os.path.join(folder_path, f"{name}({count}){ext}")
        count += 1

    return candidate


def write_log(filename, src, dst):
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_PATH, "a", encoding="utf-8") as log:
        log.write(f"{time} | {filename} | {src} → {dst}\n")


def organize():
    for file in os.listdir(BASE_DIR):

        # 이미 정리된 폴더는 무시
        if file in RULES.keys() or file == "Others":
            continue

        src = os.path.join(BASE_DIR, file)

        if os.path.isfile(src):
            ext = os.path.splitext(file)[1].lower()
            target_folder = get_folder(ext)
            target_path = os.path.join(BASE_DIR, target_folder)

            os.makedirs(target_path, exist_ok=True)
            dst = get_unique_path(target_path, file)

            shutil.move(src, dst)
            write_log(file, src, dst)
            print(f"[AutoFold] {file} 정리 완료")
