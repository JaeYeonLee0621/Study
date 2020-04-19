from abc import (
    ABCMeta,
    abstractmethod,
)


class AbstractOperationFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_operation_product(self):
        pass

    @abstractmethod
    def create_number_operand_product(self, value):
        pass


class AbstractOperationProduct(metaclass=ABCMeta):
    def __init__(self):
        self.first_num_operand_product = None
        self.second_num_operand_product = None

    def set_first_num_operand_product(self, first_num_operand_product):
        self.first_num_operand_product = first_num_operand_product

    def set_second_num_operand_product(self, second_num_operand_product):
        self.second_num_operand_product = second_num_operand_product

    def add(self):
        return self.get_first_num() + self.get_second_num()

    def get_first_num(self):
        return self.first_num_operand_product.get_number()

    def get_second_num(self):
        return self.second_num_operand_product.get_number()


class AbstractNumberOperandProduct(metaclass=ABCMeta):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def get_number(self):
        pass

    def get_value(self):
        return self.value


class DoubleOperationFactory(AbstractOperationFactory):
    def create_operation_product(self):
        return DoubleOperationProduct()

    def create_number_operand_product(self, value):
        return DoubleNumberOperandProduct(value)


class DoubleOperationProduct(AbstractOperationProduct):
    def print(self):
        return self.add()


class DoubleNumberOperandProduct(AbstractNumberOperandProduct):
    def __init__(self, value):
        AbstractNumberOperandProduct.__init__(self, value)

    def get_number(self):
        return float(self.get_value())


class Client:
    def main(self):
        operation_factory = DoubleOperationFactory()
        operation_product = operation_factory.create_operation_product()
        operation_product.set_first_num_operand_product(operation_factory.create_number_operand_product(10))
        operation_product.set_second_num_operand_product(operation_factory.create_number_operand_product(20))
        operation_product.print()
