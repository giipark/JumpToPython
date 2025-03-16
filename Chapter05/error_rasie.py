class Bird:
    def fly(self):
        raise NotImplementedError   # 자식 클래스는 반드시 fly 함수를 구현해야 함

class Eagle(Bird):
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly()