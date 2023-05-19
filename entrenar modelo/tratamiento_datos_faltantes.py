import pandas as pd
import tkinter as tk
from tkinter import scrolledtext

df = pd.read_csv("water_potability.csv", header=0)

# Función para centrar la ventana
def set_window_center(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

# Cantidad de datos nulos por variables
# Se observa que las variables con datos faltantes son ph, sulfate y Trihalomethanes

print(df.isnull().sum())

df["ph"].interpolate(method='linear', limit_direction='forward', inplace=True)
df["Sulfate"].interpolate(method='linear', limit_direction='forward', inplace=True)
df['Trihalomethanes'].interpolate(method='linear', limit_direction='forward', inplace=True)
df = df.dropna(subset=["ph"])

# Crear la ventana
window = tk.Tk()
window.title("Datos faltantes por variables")

# Crear un widget de desplazamiento de texto
scroll_text = scrolledtext.ScrolledText(window, width=40, height=10)

# Obtener los datos faltantes por variables y agregarlos al widget de desplazamiento de texto
missing_data = df.isnull().sum()
scroll_text.insert(tk.INSERT, missing_data)

# Desactivar la edición del widget de desplazamiento de texto
scroll_text.configure(state='disabled')

# Colocar el widget de desplazamiento de texto en la ventana
scroll_text.pack()

# Ajustar el tamaño y la posición de la ventana
set_window_center(window)

# Iniciar el bucle principal de la ventana
window.mainloop()


