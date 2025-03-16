class MyError(Exception):
    def __str__(self):
        return "__str__메서드는 오류 메시지를 print 문으로 출력할 경우에 호출되는 메서드"

def say_nick(nick):
    if nick == 'stupid':
        raise MyError()
    print(nick)

try:
    say_nick("angel")
    say_nick("stupid")
except MyError as e:
    print(e)
    print("허용되지 않는 별명입니다.")
