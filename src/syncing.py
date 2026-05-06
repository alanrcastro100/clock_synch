from colorama import Fore, Style
from .node import Node

text_line = Style.BRIGHT + Fore.CYAN + "\n --------------//-------------- \n"

class ClockSynchronizer:
    def __init__(self,):
        average_time = 0.0

    def clock_adjust(self, clock):
        average = self.average_time
        client_clock = clock
        client_clock = average - client_clock
        
        if abs(client_clock) % 1 > 0.60:
            if client_clock < 0:
                client_clock = client_clock - 0.40
                return client_clock
            else:
                client_clock = client_clock + 0.40
                return client_clock
        else:
            return client_clock

    def synch(self, server, client1, client2, client3):
        print("Sincronizando relógios...")
        print(f"Servidor: {server.local_clock:.2f}")
        print(f"{client1.name}: {client1.local_clock:.2f} (enviado em {client1.sent_time:.2f})")
        print(f"{client2.name}: {client2.local_clock:.2f} (enviado em {client2.sent_time:.2f})")
        print(f"{client3.name}: {client3.local_clock:.2f} (enviado em {client3.sent_time:.2f})")

        # Calculao de tempo médio
        total_time = server.local_clock + client1.local_clock + client2.local_clock + client3.local_clock
        self.average_time = total_time / 4

        print(text_line)

        print(Style.BRIGHT + Fore.GREEN + "Clock Lógico: " + Fore.CYAN + f"{self.average_time:.2f}")

        print(Style.BRIGHT + Fore.GREEN + f"\nAjuste do Clock {server.name}: " + Fore.CYAN + f"{self.clock_adjust(server.local_clock):.2f}")
        print(Style.BRIGHT + Fore.GREEN + f"\nAjuste do Clock {client1.name}: " + Fore.CYAN + f"{self.clock_adjust(client1.local_clock):.2f}")
        print(Style.BRIGHT + Fore.GREEN + f"\nAjuste do Clock {client2.name}: " + Fore.CYAN + f"{self.clock_adjust(client2.local_clock):.2f}")
        print(Style.BRIGHT + Fore.GREEN + f"\nAjuste do Clock {client3.name}: " + Fore.CYAN + f"{self.clock_adjust(client3.local_clock):.2f}")
        
        # Definir ordem real de envio ajustado pelo tempo médio (clock lógico)
        clients = [client1, client2, client3]
        clients.sort(key=lambda c: (c.sent_time - self.average_time - c.local_clock))

        print(text_line)
        print(Fore.LIGHTYELLOW_EX + "Primeiro a enviar: " + Fore.CYAN + clients[0].name + "\n"
              + Style.RESET_ALL + f" ---> (Hora de envio: {clients[0].sent_time + self.clock_adjust(clients[0].local_clock):.2f})")
        print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + "Segundo a enviar: " + Fore.CYAN + clients[1].name + "\n"
              + Style.RESET_ALL + f" ---> (Hora de envio: {clients[1].sent_time + self.clock_adjust(clients[1].local_clock):.2f})")
        print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + "Terceiro a enviar: " + Fore.CYAN + clients[2].name + "\n"
              + Style.RESET_ALL + f" ---> (Hora de envio: {clients[2].sent_time + self.clock_adjust(clients[2].local_clock):.2f})")
        print(text_line)