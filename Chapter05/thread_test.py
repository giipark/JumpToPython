import time
import threading

lock = threading.Lock()  # ✅ print 동기화용 Lock

def long_task():
    for i in range(5):
        time.sleep(1)
        with lock:  # ✅ print() 실행 시 한 번에 출력되도록 보호
            print("working:%s\n" % i)


print("Start")

threads = []
for i in range(5):
    t = threading.Thread(target=long_task)  # 스레드를 생성
    threads.append(t)

for t in threads:
    t.start()   # 스레드를 실행

for t in threads:
    t.join()    # join으로 스레드가 종료될때까지 기다림

print("End")

"""
- Python의 GIL(Global Interpreter Lock) 때문에 완전한 병렬 실행이 안 됨
- 출력 중간에 다른 스레드가 개입할 수 있어서 순서가 깨질 수 있음

working:0

working:0

working:0
working:0
working:0



일정한 간격대로 출력되는 것이 아니라, 위와 같은 결과값이 출력될 수 있음
"""