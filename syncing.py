from colorama import Fore, Style

text_line = Style.BRIGHT + Fore.CYAN + "\n --------------//-------------- \n"

class ClockSynchronizer:
    def __init__(self,):
        pass

    def synch(self, server, client1, client2, client3):
        print("Sincronizando relógios...")
        print(f"Servidor: {server.local_clock:.2f}")
        print(f"{client1.name}: {client1.local_clock:.2f} (enviado em {client1.sent_time:.2f})")
        print(f"{client2.name}: {client2.local_clock:.2f} (enviado em {client2.sent_time:.2f})")
        print(f"{client3.name}: {client3.local_clock:.2f} (enviado em {client3.sent_time:.2f})")

        # Calculao de tempo médio
        total_time = server.local_clock + client1.local_clock + client2.local_clock + client3.local_clock
        average_time = total_time / 4

        print(text_line)

        print(Style.BRIGHT + Fore.GREEN + "Clock Lógico: " + Fore.CYAN + f"{average_time:.2f}")

        print(Style.BRIGHT + Fore.GREEN + f"\nAjuste do Clock {server.name}: " + Fore.CYAN + f"{average_time - server.local_clock:.2f}")
        print(Style.BRIGHT + Fore.GREEN + f"\nAjuste do Clock {client1.name}: " + Fore.CYAN + f"{average_time - client1.local_clock:.2f}")
        print(Style.BRIGHT + Fore.GREEN + f"\nAjuste do Clock {client2.name}: " + Fore.CYAN + f"{average_time - client2.local_clock:.2f}")
        print(Style.BRIGHT + Fore.GREEN + f"\nAjuste do Clock {client3.name}: " + Fore.CYAN + f"{average_time - client3.local_clock:.2f}")
        
        # Definir ordem real de envio ajustado pelo tempo médio (clock lógico)
        clients = [client1, client2, client3]
        clients.sort(key=lambda c: (c.sent_time - average_time - c.local_clock))

        print(text_line)
        print(Fore.LIGHTYELLOW_EX + "Primeiro a enviar: " + Fore.CYAN + clients[0].name + "\n"
              + Fore.LIGHTYELLOW_EX + "Segundo a enviar: " + Fore.CYAN + clients[1].name + "\n"
              + Fore.LIGHTYELLOW_EX + "Terceiro a enviar: " + Fore.CYAN + clients[2].name)
        print(text_line)