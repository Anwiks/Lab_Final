import pandas as pd
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv("water_potability.csv", header = 0)

# Función para centrar la ventana
def set_window_center(fig):
    # Obtener el tamaño de la ventana
    window_width, window_height = fig.get_size_inches() * fig.dpi
    screen_width, screen_height = plt.gcf().canvas.get_tk_widget().winfo_screenwidth(), plt.gcf().canvas.get_tk_widget().winfo_screenheight()
    x = int((screen_width - window_width) / 2)
    y = int((screen_height - window_height) / 2)
    fig.canvas.manager.window.wm_geometry(f"+{x}+{y}")

#Variable respuesta: Potability
#1: Potable
#2: No potable

#Prueba de independencia Chi cuadrado--------------------------------
variables = df.columns.drop(["Potability"])
# Realizar prueba de chi-cuadrado para cada par de variables
for variable in variables:
    tabla_contingencia = pd.crosstab(df[variable], df['Potability'])
    chi2, p_value, dof, expected = chi2_contingency(tabla_contingencia)
    print("Para la variable", variable)
    print("El estadístico de chi-cuadrado es:", chi2)
    print("El valor p es:", p_value)
    if (p_value<0.05):
        print("Son dependientes")
    else:
        print("Son independientes")

#Analisis Grafico--------------------------------------------------------     
counts = df['Potability'].value_counts()
labels = counts.index.tolist()
values = counts.values.tolist()
colors = ["#7F95D1", "#FF82A9"]
plt.figure(num='Analisis Grafico')
plt.pie(values, labels=labels, colors = colors, autopct='%1.1f%%', )
set_window_center(plt.gcf())
plt.show()

#Diagramas de caja y bigotes de la distribucion de las variables con respecto a la potabilidad
colores = ["#7F95D1", "#FF82A9"]

#PH----
plt.figure(num="PH", figsize=(8, 5))
sns.boxplot(x='Potability', y='ph', data=df, palette = colors)
plt.xlabel('Potabilidad')
plt.ylabel('ph')
plt.title('Diagrama de caja y bigotes del nivel de ph con respecto a la potabilidad del agua')
set_window_center(plt.gcf())
plt.show()

#Hardness----
plt.figure(num="Hardness", figsize=(8, 5))
sns.boxplot(x='Potability', y='Hardness', data=df, palette = colors)
plt.xlabel('Potabilidad')
plt.ylabel('Hardness')
plt.title('Diagrama de caja y bigotes de Hardness con respecto a la potabilidad del agua')
set_window_center(plt.gcf())
plt.show()

#Solids----
plt.figure(num="Solids", figsize=(8, 5))
sns.boxplot(x='Potability', y='Solids', data=df, palette = colors)
plt.xlabel('Potabilidad')
plt.ylabel('Solids')
plt.title('Diagrama de caja y bigotes de Solids con respecto a la potabilidad del agua')
set_window_center(plt.gcf())
plt.show()

#Chloramines---
plt.figure(num="Chloramines", figsize=(8, 5))
sns.boxplot(x='Potability', y='Chloramines', data=df, palette = colors)
plt.xlabel('Potabilidad')
plt.ylabel('Chloramines')
plt.title('Diagrama de caja y bigotes de Chloramines con respecto a la potabilidad del agua')
set_window_center(plt.gcf())
plt.show()

#Sulfate-----
plt.figure(num="Sulfate", figsize=(8, 5))
sns.boxplot(x='Potability', y='Sulfate', data=df, palette = colors)
plt.xlabel('Potabilidad')
plt.ylabel('Sulfate')
plt.title('Diagrama de caja y bigotes de Sulfate con respecto a la potabilidad del agua')
set_window_center(plt.gcf())
plt.show()

#Conductivity----
plt.figure(num="Conductivity", figsize=(8, 5))
sns.boxplot(x='Potability', y='Conductivity', data=df, palette = colors)
plt.xlabel('Potabilidad')
plt.ylabel('Conductivity')
plt.title('Diagrama de caja y bigotes de Conductivity con respecto a la potabilidad del agua')
set_window_center(plt.gcf())
plt.show()

#Organic_carbon-----
plt.figure(num="Organic carbon", figsize=(8, 5))
sns.boxplot(x='Potability', y='Organic_carbon', data=df, palette = colors)
plt.xlabel('Potabilidad')
plt.ylabel('Organic_carbon')
plt.title('Diagrama de caja y bigotes de Organic_carbon con respecto a la potabilidad del agua')
set_window_center(plt.gcf())
plt.show()

#Trihalomethanes-----
plt.figure(num="Trihalomethanes",figsize=(8, 5))
sns.boxplot(x='Potability', y='Trihalomethanes', data=df, palette = colors)
plt.xlabel('Potabilidad')
plt.ylabel('Trihalomethanes')
plt.title('Diagrama de caja y bigotes de Trihalomethanes con respecto a la potabilidad del agua')
set_window_center(plt.gcf())
plt.show()

#Turbidity-----
plt.figure(num="Turbidity",figsize=(8, 5))
sns.boxplot(x='Potability', y='Turbidity', data=df, palette = colors)
plt.xlabel('Potabilidad')
plt.ylabel('Turbidity')
plt.title('Diagrama de caja y bigotes de Turbidity con respecto a la potabilidad del agua')
set_window_center(plt.gcf())
plt.show()

#Matris de Correlación entre las variables------------------------------
matriz_cor = df.drop("Potability", axis = 1).corr()
print(matriz_cor)

#Mapa de calor
fig, ax = plt.subplots(num="Mapa de calor")
im = ax.imshow(matriz_cor)
cbar = ax.figure.colorbar(im, ax = ax)
cbar.ax.set_ylabel("Coeficiente de Correlación", rotation = -90, va = "bottom")
set_window_center(plt.gcf())
plt.show()
