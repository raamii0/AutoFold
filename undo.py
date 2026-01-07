import os
import shutil

LOG_PATH = "logs/history.log"

def undo():
    if not os.path.exists(LOG_PATH):
        print("[AutoFold] 되돌릴 기록이 없다.")
        return

    with open(LOG_PATH, "r", encoding="utf-8") as log:
        lines = log.readlines()

    for line in lines:
        try:
            _, filename, paths = line.strip().split(" | ")
            src, dst = paths.split(" → ")

            if os.path.exists(dst):
                os.makedirs(os.path.dirname(src), exist_ok=True)
                shutil.move(dst, src)
                print(f"[AutoFold] 되돌림 완료: {filename}")
        except:
            continue

    # 로그 초기화 (한 번만 되돌리도록)
    open(LOG_PATH, "w", encoding="utf-8").close()
    print("[AutoFold] 모든 파일 되돌리기 완료")

if __name__ == "__main__":
    undo()
