from abc import (
    ABCMeta,
    abstractmethod,
)


class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.build_first_num()
        self.builder.build_operator()
        self.builder.build_second_num()
        self.builder.build_answer()

        result = self.builder.get_result()
        self._print(result)

    def _print(self, result):
        print(result)


class AbstractOperationBuilder(metaclass=ABCMeta):
    def __init__(self, first_num, second_num):
        self.result = ''
        self.first_num = first_num
        self.second_num = second_num

    @abstractmethod
    def operate(self, first_num, second_num):
        pass

    @abstractmethod
    def build_operator(self):
        pass

    def build_first_num(self):
        self.result += str(self.first_num)

    def build_second_num(self):
        self.result += str(self.second_num)

    def get_result(self):
        return self.result


class AddOperationBuilder(AbstractOperationBuilder):
    def __init__(self, first_num, second_num):
        AbstractOperationBuilder.__init__(first_num, second_num)

    def operate(self, first_num, second_num):
        return first_num + second_num

    def build_operator(self):
        self.result += '+'


class Client:
    def main(self):
        Director(AddOperationBuilder(10, 20)).construct()
