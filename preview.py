import os
from config import BASE_DIR, RULES
from organizer import get_folder

def preview():
    print("[AutoFold] 미리보기 시작\n")

    for file in os.listdir(BASE_DIR):
        src = os.path.join(BASE_DIR, file)

        if os.path.isfile(src):
            ext = os.path.splitext(file)[1].lower()
            target = get_folder(ext)

            print(f"{file}  →  {target}/")

    print("\n[AutoFold] 미리보기 종료")
