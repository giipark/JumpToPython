import time

def longtime_job():
    print("job start")
    time.sleep(0.5)
    return "done"

# 'list comprehension' 내에서 한번 실행된 후, 결과가 한번에 리스트에 저장
list_job = [longtime_job() for i in range(5)]
print(list_job[0])
print(list_job)
print("=" * 50)
# ================================================================================================
# 함수 실행을 즉시 하지 않고, 'lambda'를 사용하여 나중에 실행되도록 변경
list_job2 = [lambda: longtime_job() for i in range(5)]
print(list_job2[0]())
print(list_job2[1]())
print("=" * 50)
# ================================================================================================
# generator를 사용하여 실행을 지연 (lazy evaluation)
list_job3 = (longtime_job() for i in range(5))
print(next(list_job3))
print(next(list_job3))