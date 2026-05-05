from src import client, server, syncing

if __name__ == "__main__":
    print("\nSistema de Sincronização de Relógios\n")

    server1 = server.Server("Servidor")
    client1 = client.Client("Cliente 1")
    client2 = client.Client("Cliente 2")
    client3 = client.Client("Cliente 3")

    synchronizer = syncing.ClockSynchronizer()

    synchronizer.synch(server1, client1, client2, client3)
