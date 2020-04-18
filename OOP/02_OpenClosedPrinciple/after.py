'''
calculate 라는 함수가 아닌 add, divide 즉 기능별로 함수를 분류해서
기능이 추가될 때마다 calculate 함수가 수정되는 것이 아닌 기능을 추가하도록 만든다
'''


class AddOperation:
    def operate(self, first_num, second_num):
        return first_num + second_num


class DivideOperation:
    def operate(self, first_num, second_num):
        return first_num / second_num


class Calculator:
    def __init__(self):
        self.add_operation = None
        self.divide_operation = None

    def set_add_operation(self, add_operation):
        self.add_operation = add_operation

    def set_divide_operation(self, divide_operation):
        self.divide_operation = divide_operation

    def add(self, first_num, second_num):
        return self.add_operation.operate(first_num, second_num)

    def divide(self, first_num, second_num):
        return self.divide_operation.operate(first_num, second_num)


class Client:
    def main(self):
        calculator = Calculator()
        calculator.set_add_operation(AddOperation())
        calculator.set_divide_operation(DivideOperation())
        calculator.add(1, 2)
        calculator.divide(1, 2)
