import sys


class ConsoleMessenger(object):

    def __init__(self):
        object.__init__(self)

    def send(self, message):
        """ Print all the products information passed in message.
            :param message: A objects list of type Products.
        """
        for product in message:
            sys.stdout.write(product.__str__())
