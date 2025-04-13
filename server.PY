# serveur.py
import socket
import threading

def recevoir(client):
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
            if not msg:
                break
            print("\nClient :", msg)
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
    serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serveur.bind(('', 3000))
    serveur.listen(1)
    print("Serveur en attente d'une connexion...")

    client, infosclient = serveur.accept()
    print("Client connecté depuis", infosclient)

    thread_reception = threading.Thread(target=recevoir, args=(client,))
    thread_envoi = threading.Thread(target=envoyer, args=(client,))
    
    thread_reception.start()
    thread_envoi.start()

    thread_reception.join()
    thread_envoi.join()

    client.close()
    serveur.close()

if __name__ == "__main__":
    main()
