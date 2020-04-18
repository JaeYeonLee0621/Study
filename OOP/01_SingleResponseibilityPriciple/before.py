class Calaulator:

    def calculate(self, operator, first_num, second_num):
        '''
        Calculator class
        현재 calculate 라는 함수 안에 /, + 두 개의 기능이 존재한다
        이는 한 개의 class 가 하나의 기능을 가져야 한다는 것에 위배된다
        '''
        answer = 0
        if operator == '/':
            answer = first_num / second_num
        if operator == '+':
            answer = first_num + second_num
        return answer


class Client:
    def main(self):
        calculator = Calaulator()
        calculator.calculate('/', 1, 2)
        calculator.calculate('+', 1, 2)
