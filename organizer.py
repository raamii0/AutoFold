import os
import shutil
from config import BASE_DIR, RULES

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

def organize():
    for file in os.listdir(BASE_DIR):
        src = os.path.join(BASE_DIR, file)

        if os.path.isfile(src):
            ext = os.path.splitext(file)[1].lower()
            target_folder = get_folder(ext)
            target_path = os.path.join(BASE_DIR, target_folder)

            os.makedirs(target_path, exist_ok=True)
            dst = get_unique_path(target_path, file)

            shutil.move(src, dst)
            print(f"[AutoFold] {file} 정리 완료")
