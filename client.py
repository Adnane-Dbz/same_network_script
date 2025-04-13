# client.py
import socket
import threading

def recevoir(client):
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
            if not msg:
                break
            print("\nServeur :", msg)
        except:
            break

def envoyer(client):
    while True:
        try:
            msg = input()
            client.send(msg.encode('utf-8'))
        except:
            break

def main():
    addrPort = ("127.0.0.1", 3000)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(addrPort)
    print("Connecté au serveur.")

    thread_reception = threading.Thread(target=recevoir, args=(client,))
    thread_envoi = threading.Thread(target=envoyer, args=(client,))

    thread_reception.start()
    thread_envoi.start()

    thread_reception.join()
    thread_envoi.join()

    client.close()

if __name__ == "__main__":
    main()
