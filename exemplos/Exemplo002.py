import socket

hostname = socket.gethostname()
ip_local = socket.gethostbyaddr(hostname)

print (f"Nome do host: {hostname}")
print (f"IP local: {ip_local}")