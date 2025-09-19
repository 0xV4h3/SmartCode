from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar("T", bound="Transport")


class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass


class Truck(Transport):
    def deliver(self):
        print("Delivered by the truck")


class Ship(Transport):
    def deliver(self):
        print("Delivered by the ship")


class Logistic(ABC, Generic[T]):
    def __init__(self, transport: T):
        self._transport = transport

    @property
    def transport(self) -> T:
        return self._transport

    @transport.setter
    def transport(self, transport: T):
        if isinstance(transport, Transport):
            self._transport = transport
        else:
            raise TypeError("Transport must be an instance of Transport")

    @abstractmethod
    def cargo(self):
        pass


class LandLogistic(Logistic[Truck]):
    def __init__(self, transport: Truck):
        super().__init__(transport)

    def cargo(self):
        self.transport.deliver()


class SeaLogistic(Logistic[Ship]):
    def __init__(self, transport: Ship):
        super().__init__(transport)

    def cargo(self):
        self.transport.deliver()


if __name__ == "__main__":
    truck = Truck()
    landlog = LandLogistic(truck)
    landlog.cargo()
    ship = Ship()
    sealog = SeaLogistic(ship)
    sealog.cargo()