import socket

# Creamos un socket TCP/IP
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectamos el cliente al servidor
direccion_servidor = ('localhost', 8888)
cliente.connect(direccion_servidor)

# Recibimos el menú del servidor
menu = cliente.recv(1024).decode()
print(menu)

# Solicitamos la elección al usuario
eleccion = input("Ingrese su elección: ")

# Enviamos la elección al servidor
cliente.send(eleccion.encode())

# Recibimos la respuesta del servidor
respuesta = cliente.recv(4096).decode()
print(respuesta)

# Cerramos la conexión con el servidor
cliente.close()
