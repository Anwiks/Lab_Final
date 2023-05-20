import socket

# Creamos un socket TCP/IP
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Asignamos una dirección y un puerto al servidor
direccion_servidor = ('localhost', 8888)
servidor.bind(direccion_servidor)

# Escuchamos conexiones entrantes
servidor.listen(1)

print("El servidor está listo para recibir conexiones...")

while True:
    # Esperamos a que un cliente se conecte
    cliente, direccion_cliente = servidor.accept()
    print(f"Cliente conectado desde: {direccion_cliente}")

    # Enviamos el menú al cliente
    menu = "Por favor, seleccione una opción:\n1. Tratamiento de datos faltantes\n2. Análisis descriptivo\n3. Modelo\n"
    cliente.send(menu.encode())

    # Recibimos la elección del cliente
    eleccion = cliente.recv(1024).decode()

    if eleccion == "1":
        # Ejecutar código de tratamiento de datos faltantes
        import tratamiento_datos_faltantes as tdf
        code = tdf.tratamiento_datos_faltantes()
        cliente.send(code.encode())
    elif eleccion == "2":
        # Ejecutar código de análisis descriptivo
        import analisis_descriptivo as ad
        code = ad.analisis_descriptivo()
        cliente.send(code.encode())
    elif eleccion == "3":
        # Ejecutar código de modelo
        import modelo as mdl
        code = mdl.modelo()
        cliente.send(code.encode())
    else:
        mensaje_error = "Opción inválida"
        cliente.send(mensaje_error.encode())

    # Cerramos la conexión con el cliente
    cliente.close()










