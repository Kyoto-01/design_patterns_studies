#!/usr/bin/env python3

from abc import ABC, abstractmethod
from time import sleep
from threading import Thread

# Abstract Factory
class Worker(ABC):

    def __init__(self, name: "str"):
        self.__name: "str" = name
        self.__action: "str" = None

    @property
    def action(self):
        return self.__action
    
    @action.setter
    def action(self, value: "str"):
        self.__action = value
        if value != "":
            print(self.__name, ": ", self.__action)
            sleep(1)
    
    @abstractmethod
    def work(self):
        pass


class Master(Worker):

    def __init__(self, name: "str"):
        super().__init__(name)

    def work(self):
        self.action = "Wake up"
        self.action = "Eat"
        self.action = "Dance a little"
        self.action = "Walk"
        self.action = "Lazy Work"
        self.action = "Hard Work"
        self.action = "Hard Work"
        self.action = "Rest"
        self.action = ""


# Observer
class Slave(Worker):

    def __init__(self, master: "Master", name: "str"):
        self.__master = master
        super().__init__(name)

    def work(self):
        while self.action != "":
            if self.__master.action == "Hard Work":
                shovel = Shovel()
                self.action = self.__master.action
                del shovel
            else:
                self.action = self.__master.action

# Singleton
class Shovel:

    __INSTANCE = None

    def __new__(cls):
        if cls.__INSTANCE is None:
            cls.__INSTANCE = super().__new__(cls)
            print("Get shovel!")
        else:
            print("Shovel in use!!!!")

        return cls.__INSTANCE

    def __init__(self):
        self.__state: "str" = None

    @property
    def state(self):
        return self.__state
    
    @state.setter
    def state(self, value: "str"):
        self.__state = value

    def __del__(self):
        self.__INSTANCE = None


def main(numSlaves: "int"):
    master = Master("Master1")
    slaves = [Slave(master, f"Slave{i}") for i in range(numSlaves)]

    Thread(target=master.work).start()
    for slave in slaves:
        Thread(target=slave.work).start()


if __name__ == "__main__":
    main(4)
