'''
추상 클래스로 변경하여 해당 추상 킁래스를 사용하는 식으로 의존성을 제거한다
'''

from abc import (
    ABCMeta,
    abstractmethod,
)


class AbstractOperation(metaclass=ABCMeta):
    @abstractmethod
    def operate(self, first_num, second_num):
        pass

    def is_invalid_num(self, first_num, second_num):
        return False


class AddOperation(AbstractOperation):
    def operate(self, first_num, second_num):
        return first_num + second_num


class DivideOperation(AbstractOperation):
    def operate(self, first_num, second_num):
        return first_num / second_num

    def is_invalid_num(self, first_num, second_num):
        return second_num == 0


class Calculator:
    def __init__(self):
        self.operation = None

    def set_operation(self, operation):
        self.operation = operation

    def calculate(self, first_num, second_num):
        if self.operation.is_invalid_num(first_num, second_num):
            return -999
        return self.operation.operate(first_num, second_num)


class Client:
    def main(self):
        calculator = Calculator()
        calculator.set_operation(AddOperation())
        calculator.calculate(1, 2)
