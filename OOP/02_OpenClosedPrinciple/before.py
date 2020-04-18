'''
이 코드에서 기능을 추가하려면 calculate 함수에서 조건문을 추가하는 방식으로 가야한다
그렇다면 확장에는 열리고 변경에는 닫혀있는 원칙에 위배된다
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
