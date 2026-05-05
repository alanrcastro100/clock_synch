from colorama import Fore, Style


class Node:
    def __init__(self, name):
        self.name = name
        self.local_clock = 0.0
        self.sent_time = 0.0

        self.create()

    
    def get_input(self, prompt):
        while True:
            try:
                return float(input(Fore.YELLOW + Style.BRIGHT + prompt + Style.RESET_ALL))
            except ValueError:
                print(Fore.RED + "** Digite números válidos! **\n" + Style.RESET_ALL)

    def create(self):
        print(f"Criando '{self.name}'")
        self.local_clock = self.get_input("Digite a hora: ")
        self.sent_time = self.get_input("Digite a hora de envio: ")
        print("Dados salvos!\n")