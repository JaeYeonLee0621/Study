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
        '''
        나누기 연산시 나눌 숫자는 0이 아니면 안된다는 validation을 추가한다
        만약 해당 class 를 다른 calculator class에서 또 사용한다고 가정해보자
        그렇다면 그 클래스에서도 마찬가지로 해당 기능을 구현해줘야한다
        만약 많은 class에서 DivideOperaion을 사용하고 있다면
        해당 validation 을 많은 class에서 추가해줘야한다
        만약 조건이 변경된다고 하자
        그렇다면 그 많은 class를 찾아가 모든 조건을 변경해야한다
        '''
        if isinstance(property, DivideOperation) and second_num == 0: return -999
        return self.operation.operate(first_num, second_num)


class Client:
    def main(self):
        calculator = Calculator()
        calculator.set_operation(AddOperation())
        calculator.calculate(1, 2)
