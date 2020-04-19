class Singleton:
    # Private
    __instance = None

    @classmethod
    def get_instance(cls, *args, **kwargs):
        if not cls.__instance: cls.__instance = cls(*args, **kwargs)
        return cls.__instance


class Client:
    def main(self):
        Singleton.get_instance()
