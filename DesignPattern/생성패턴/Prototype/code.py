from abc import (
    ABCMeta,
    abstractmethod,
)


class AbstractOperationPrototype(metaclass=ABCMeta):
    def __init__(self, operation=None):
        if not operation:
            self.first_num = operation.first_num
            self.second_num = operation.second_num
        else:
            self.first_num = 0
            self.second_num = 0

    @abstractmethod
    def get_clone(self):
        pass

    def get_first_num(self):
        return self.first_num

    def get_second_num(self):
        return self.second_num

    def set_first_num(self, first_num):
        self.first_num = first_num

    def set_second_num(self, second_num):
        self.second_num = second_num

    @abstractmethod
    def get_operator(self):
        pass

    def operate(self):
        first_num = self.get_first_num()
        second_num = self.get_second_num()
        operator = self.get_operator()
        return f'{first_num}{operator}{second_num}'


class AddOperationPrototype(AbstractOperationPrototype):
    def __init__(self, operation=None):
        AbstractOperationPrototype.__init__(self, operation)

    def get_clone(self):
        return AddOperationPrototype(self)

    def get_operator(self):
        return 'plus'


class Client:
    def __init__(self):
        self.operation_prototype = None

    def operate(self):
        self.operation_prototype.operate()

    def set_operation(self, operator, first_num, second_num):
        self.operation_prototype = self.get_operation_clone(operator)
        self.operation_prototype.set_first_num(first_num)
        self.operation_prototype.set_second_num(second_num)

    def get_operation_clone(self, operator):
        if operator == '+':
            operation = AddOperationPrototype()
            return operation.get_clone()
        return None

    def main(self):
        client = Client()
        client.set_operation('+', 10, 20)
        client.operate()


