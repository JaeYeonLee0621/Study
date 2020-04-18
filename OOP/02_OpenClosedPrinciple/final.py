'''
class 로 나누는 것보다 같은 기능을 하는 것을 추상 클래스로 만들면
add, divide 함수를 만들 필요 없이 calculate 함수 하나만으로 가능하다
확장은 편해지고 수정은 적어진다
'''

from abc import (
    ABCMeta,
    abstractmethod,
)


class AbstractOperation(metaclass=ABCMeta):
    @abstractmethod
    def operate(self, first_num, second_num):
        pass


class AddOperation(AbstractOperation):
    def operate(self, first_num, second_num):
        return first_num + second_num


class DivideOperation(AbstractOperation):
    def operate(self, first_num, second_num):
        return first_num / second_num


class Calculator:
    def __init__(self):
        self.operation = None

    def set_operation(self, operation):
        self.operation = operation

    def calculate(self, first_num, second_num):
        return self.operation.operate(first_num, second_num)


class Client:
    def main(self):
        calculator = Calculator()
        calculator.set_operation(AddOperation())
        calculator.calculate(1, 2)
