import abc


class ItemCreator(metaclass=abc.ABCMeta):
    def create(self):
        self._request_item_info()
        item = self._create_item()
        self._create_item_log()
        return item

    @abc.abstractmethod
    def _request_item_info(self):
        pass

    @abc.abstractmethod
    def _create_item(self):
        pass

    @abc.abstractmethod
    def _create_item_log(self):
        pass


class Item(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def use(self):
        pass


class HpPotion(Item):
    def use(self):
        print('HP Potion 사용')


class MpPotion(Item):
    def use(self):
        print('MP Potion 사용')


class HpPotionCreator(ItemCreator):
    def _request_item_info(self):
        print('HP Potion item 정보')

    def _create_item(self):
        return HpPotion()

    def _create_item_log(self):
        print('HP Potion item 로그')


class MpPotionCreator(ItemCreator):
    def _request_item_info(self):
        print('MP Potion item 정보')

    def _create_item(self):
        return MpPotion()

    def _create_item_log(self):
        print('MP Potion item 로그')


creator = MpPotionCreator()
item = creator.create()
item.use()

creator = HpPotionCreator()
item = creator.create()
item.use()
