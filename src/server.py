from .node import Node

class Server(Node):
    def __init__(self, name):
        super().__init__(name)

    def create(self):
        print(f"Criando Servidor '{self.name}'")
        self.local_clock = self.get_input("Digite a hora do servidor: ")
        print("Servidor configurado!\n")