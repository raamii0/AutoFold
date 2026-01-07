import time
from organizer import organize
from preview import preview

print("""
[AutoFold v3]
1. 미리보기
2. 한 번만 정리
3. 계속 자동 정리
""")

mode = input("모드 선택: ")

if mode == "1":
    preview()

elif mode == "2":
    organize()
    print("[AutoFold] 한 번 정리 완료")

elif mode == "3":
    print("[AutoFold] 자동 정리 시작 (Ctrl+C 종료)")
    while True:
        organize()
        time.sleep(5)

else:
    print("잘못된 선택")
