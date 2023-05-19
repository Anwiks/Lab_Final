import tkinter as tk
from tkinter import scrolledtext
import socket
import subprocess

# Función para centrar la ventana
def set_window_center(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

# Función para enviar el resultado al cliente
def send_result_to_client(result, client_ip, client_port):
    client_address = (client_ip, client_port)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(client_address)
        sock.sendall(result.encode())

# Función para ejecutar el código y enviar el resultado al cliente
def execute_code():
    code = code_text.get('1.0', tk.END)
    result = subprocess.getoutput(code)
    client_ip = ip_entry.get()
    client_port = int(port_entry.get())
    send_result_to_client(result, client_ip, client_port)

# Crear la ventana principal
window = tk.Tk()
window.title("Enviar Código Ejecutado")

# Crear un widget de desplazamiento de texto para ingresar el código
code_text = scrolledtext.ScrolledText(window, width=80, height=20)
code_text.pack()

# Crear el campo de entrada para la dirección IP del cliente
ip_label = tk.Label(window, text="Dirección IP del Cliente:")
ip_label.pack()
ip_entry = tk.Entry(window)
ip_entry.pack()

# Crear el campo de entrada para el puerto del cliente
port_label = tk.Label(window, text="Puerto del Cliente:")
port_label.pack()
port_entry = tk.Entry(window)
port_entry.pack()

# Crear el botón para ejecutar y enviar el código
execute_button = tk.Button(window, text="Ejecutar y Enviar Código", command=execute_code)
execute_button.pack(pady=10)

# Ajustar el tamaño y la posición de la ventana
set_window_center(window)

# Iniciar el bucle principal de la ventana
window.mainloop()











