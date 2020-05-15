import abc


class Math:
    @staticmethod
    def twice(num):
        return num * 2

    @staticmethod
    def half(num):
        return num / 2


'''
python은 interface라는 개념이 없다
단지 abstract라는 개념이 있을 뿐이다
만약 interface를 생성하고 싶다면 Metaclass를 이용하여 __subclasscheck__ 을 custom하고 사용할 수 있다
'''


class Adapter(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def twice(self, num):
        pass

    @abc.abstractmethod
    def half(self, num):
        pass


class Adaptee(Adapter):
    def twice(self, num):
        return float(Math.twice(num))

    def half(self, num):
        return float(Math.half(num))


adaptee = Adaptee()
print(adaptee.half(10))
print(adaptee.twice(10))
