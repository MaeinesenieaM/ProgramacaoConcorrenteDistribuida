#Servidor!
import socket
from datetime import datetime

def start_server():
    HOST = "127.0.0.1"
    PORT = 30303

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen()
        print(f"Servidor esperando por requisitos em {HOST}:{PORT}")

        while True:
            conn, addr = server.accept()
            with conn:
                print(f"Conexão com {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    if data.decode() == "data e hora":
                        now = datetime.now().strftime("%Y - %m - %d %H:%M:%S")
                        message = f"Data e hora: {now}"
                        conn.sendall(message.encode())
                    else:
                        message = "Mensagem invalida!"
                        conn.sendall(message.encode())

if __name__ == "__main__":
    start_server()