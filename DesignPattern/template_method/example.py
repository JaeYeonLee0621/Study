import abc


class GameConnectHelper(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def do_security(self):
        pass

    @abc.abstractmethod
    def authentication(self):
        pass

    @abc.abstractmethod
    def authorization(self):
        pass

    @abc.abstractmethod
    def connect(self):
        pass

    def request_connection(self):
        self.do_security()
        self.authentication()
        self.authorization()
        self.connect()
        print('연결 되었습니다.')


class Connection(GameConnectHelper):
    def do_security(self):
        print('보안 과정 진행')

    def authentication(self):
        print('인증')

    def authorization(self):
        print('권한 확인')

    def connect(self):
        print('연결 완료')


connect = Connection()
connect.request_connection()