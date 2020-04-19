from abc import (
    ABCMeta,
    abstractmethod,
)


class AbstractOperation(metaclass=ABCMeta):
    def __init__(self):
        self.first_num = 0
        self.second_num = 0

    def operate(self):
        first_num = self.get_first_num()
        second_num = self.get_second_num()
        operator = self.get_operator()
        operator_description = operator.get_description()
        return f'{operator_description} : {first_num}{operator}{second_num}'

    @abstractmethod
    def get_operator(self):
        pass

    def get_first_num(self):
        return self.first_num

    def set_first_num(self, first_num):
        self.first_num = first_num

    def get_second_num(self):
        return self.second_num

    def set_second_num(self, second_num):
        self.second_num = second_num


class AbstractOperator(metaclass=ABCMeta):
    @abstractmethod
    def get_description(self):
        pass


class AddOperator(AbstractOperator):
    def get_description(self):
        return 'plus'


class AddOperation(AbstractOperation):
    def get_operator(self):
        return AddOperator()


class Client:
    def main(self):
        operation = AddOperation()
        operation.set_first_num(10)
        operation.set_second_num(20)
        operation.operate()