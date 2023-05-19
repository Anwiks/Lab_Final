import socket

# Dirección IP y puerto del servidor
server_address = ('<server_ip>', 12345)  # Remplace <server_ip> con el ip del pc donde esta el codigo principal

# Crear un socket TCP/IP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Conectar al servidor
    sock.connect(server_address)

    # Recibir el resultado del servidor
    result = sock.recv(4096).decode()

    # Mostrar el resultado recibido
    print("Resultado recibido:")
    print(result)
