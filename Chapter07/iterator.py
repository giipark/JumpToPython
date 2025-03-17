class MyIterator:
    def __init__(self, data):
        self.data = data
        self.position = 0

    # '__iter__'메서드를 구현하면, 해당 클래스는 반복 가능한 객체가 됨
    def __iter__(self):
        return self

    # '__iter__'를 구현할 경우, 반드시 '__next__'함수를 구현해야 함
    # 구현 안할시 오류발생: TypeError: iter() returned non-iterator of type 'MyIterator'
    def __next__(self):
        if self.position >= len(self.data):
            raise StopIteration
        result = self.data[self.position]
        self.position += 1
        return result


if __name__ == "__main__":
    i = MyIterator([1, 2, 3, 4])
    for item in i:
        print(item)
