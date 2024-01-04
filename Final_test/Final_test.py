class Chicken:
    def __init__(self, store, taste, parts, source, spiciness):
        self.store = store              #店家
        self.taste = taste              #口味
        self.parts = parts              #部位
        self.source = source            #來源
        self.spiciness = spiciness      #辣度


    @property
    def chicken_store(self):
        return self.store


    @chicken_store.setter
    def sports_name(self, value):
        self._store = value


class PartsChicken(Chicken):
    def __init__(self, store, parts):
        super().__init__(store)
        self._parts = parts


    @property
    def partschicken_parts(self):
        return self._parts


class SpicinessChicken(Chicken):
    def __init__(self, store, spiciness):
        super().__init__(store)
        self._spiciness =  spiciness


    @property
    def spicinesschicken_spiciness(self):
        return self._spiciness



#使用範例
if __name__ == "__main__":
    
    # 建立一個新的 PartsChicken對象
    store = PartsChicken("雞腿", "雞翅", "雞排", "雞胸肉")
    print(store.chicken_store)
    print(store.partschicken_parts)

    # 建立一個新的 SpicinessChicken對象
    spiciness = SpicinessChicken("不辣", "小辣", "中辣", "大辣")
    print(spiciness.chicken_store)
    print(spiciness.spicinesschicken_spiciness)

    chicken = Chicken("麥當勞", "肯德基", "胖老爹", "丹丹漢堡")
    print(chicken.chicken_store)