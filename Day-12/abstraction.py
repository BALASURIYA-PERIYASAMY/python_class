from abc import ABC, abstractmethod

class wedding(ABC):
    @abstractmethod
    def enjoy_food(self):
        print("Enjoying food...!")

class child(wedding):
    def enjoy_food(self):
        print("Eating with fingers like a child")


# wed = wedding()   # TypeError : Can't instantiate abstract class

ch = child()
ch.enjoy_food()