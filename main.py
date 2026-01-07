import time
from organizer import organize

print("[AutoFold] 실행 중... (Ctrl+C 종료)")

while True:
    organize()
    time.sleep(5)
