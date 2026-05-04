from node import Node

class Client(Node):
    def __init__(self, name):
        super().__init__(name)

    def create(self):
        super().create()