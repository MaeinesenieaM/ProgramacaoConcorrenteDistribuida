#Cliente!
import socket

def start_client():
    HOST = "127.0.0.1"
    PORT = 30303

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
        cliente.connect((HOST, PORT))
        print("Solicitando data e hora...")
        cliente.sendall(b"data e hora")
        data = cliente.recv(1024)
        print(f"Resposta do servidor: {data.decode()}")

if __name__ == "__main__":
    start_client()