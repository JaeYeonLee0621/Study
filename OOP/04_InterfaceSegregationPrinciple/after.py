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

    @abstractmethod
    def get_operator(self):
        pass


class AddOperation(AbstractOperation):
    def operate(self, first_num, second_num):
        return first_num + second_num

    def get_operator(self):
        return '+'


class DivideOperation(AbstractOperation):
    def operate(self, first_num, second_num):
        return first_num / second_num

    def get_operator(self):
        return '/'


class IDisplyable(metaclass=ABCMeta):
    @abstractmethod
    def display(self, operation):
        pass


class Calculator(IDisplyable):
    def __init__(self):
        self.operation = None

    def set_operation(self, operation):
        self.operation = operation

    def calculate(self, first_num, second_num):
        return self.operation.operate(first_num, second_num)

    def display(self):
        return self.operation.get_operator()


class CalClient:
    def request(self, calculator, operation, first_num, second_num):
        calculator.set_operation(operation)
        return calculator.calculate(first_num, second_num)


class DisplayClient:
    def request(self, displayable, operation):
        return displayable.display(operation)


class Client:
    def main(self):
        calculator = Calculator()
        cal_client = CalClient()
        cal_client.request(calculator, AddOperation(), 1, 2)
        display_client = DisplayClient()
        display_client.request(calculator, AddOperation())
