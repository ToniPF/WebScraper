import sys
from abc import ABC, abstractmethod


class IMessenger(ABC):
    @abstractmethod
    def send(self, message, destination):
        raise NotImplementedError


class ConsoleMessenger(IMessenger):

    def send(self, message, destination=sys.stdout):
        """ Print all the products information passed in message.
            :param destination: In console message stdout by default.
            :param message: A objects list of type Products.
        """
        for product in message:
            destination.write(product.__str__())
