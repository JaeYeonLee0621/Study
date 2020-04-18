'''
Operation 을 Class 로 분할하고
Calculator Class 안에서는 해당 Class 의 인스턴스를 불러오는 식으로 변경한다
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

    def calculate(self, operator, first_num, second_num):
        if operator == '+':
            return self.add_operation.operate(first_num, second_num)
        if operator == '/':
            return self.divide_operation.operate(first_num, second_num)


class Client:
    def main(self):
        calculator = Calculator()
        calculator.set_add_operation(AddOperation())
        calculator.set_divide_operation(DivideOperation())
        calculator.calculate('+', 1, 2)
        calculator.calculate('/', 1, 2)
