import sys


class ConsoleMessenger(object):

    def __init__(self):
        object.__init__(self)

    def send(self, message):
        for product in message:
            sys.stdout.write(product.__str__())
