'''
class 로 나누는 것보다 같은 기능을 하는 것을 추상 클래스로 만들면
add, divide 함수를 만들 필요 없이 calculate 함수 하나만으로 가능하다
'''

from abc import (
    ABCMeta,
    abstractmethod,
)


class AbstractOperation(metaclass=ABCMeta):
    @abstractmethod
    def operate(self, first_num, second_num):
        pass

    '''
    해당 validation을 상위 클래스로 뺀다
    '''
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
