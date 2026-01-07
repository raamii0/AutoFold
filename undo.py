import os
import shutil

# exe / py 공통 로그 경로 처리
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
LOG_PATH = os.path.join(BASE_PATH, "logs", "history.log")


def undo():
    if not os.path.exists(LOG_PATH):
        print("[AutoFold] 되돌릴 기록이 없습니다.")
        return

    with open(LOG_PATH, "r", encoding="utf-8") as log:
        lines = log.readlines()

    if not lines:
        print("[AutoFold] 되돌릴 기록이 없습니다.")
        return

    for line in lines:
        try:
            _, filename, paths = line.strip().split(" | ")
            src, dst = paths.split(" → ")

            if os.path.exists(dst):
                os.makedirs(os.path.dirname(src), exist_ok=True)
                shutil.move(dst, src)
                print(f"[AutoFold] 되돌림 완료: {filename}")

        except Exception:
            continue

    # 한 번만 되돌릴 수 있도록 로그 초기화
    open(LOG_PATH, "w", encoding="utf-8").close()
    print("[AutoFold] 모든 파일 되돌리기 완료")


if __name__ == "__main__":
    undo()
