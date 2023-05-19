from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_curve, roc_auc_score, auc
import pandas as pd
import numpy as np
import time
import statsmodels.api as sm
import matplotlib.pyplot as plt




df = pd.read_csv("water_potability.csv", header=0)

# Función para centrar la ventana
def set_window_center(fig):
    # Obtener el tamaño de la ventana
    window_width, window_height = fig.get_size_inches() * fig.dpi
    screen_width, screen_height = plt.gcf().canvas.get_tk_widget().winfo_screenwidth(), plt.gcf().canvas.get_tk_widget().winfo_screenheight()
    x = int((screen_width - window_width) / 2)
    y = int((screen_height - window_height) / 2)
    fig.canvas.manager.window.wm_geometry(f"+{x}+{y}")

# Verificar y eliminar valores faltantes
df = df.dropna()

# Verificar y eliminar valores no numéricos (si aplica)
# Si tienes variables categóricas, conviértelas en variables dummy o utiliza técnicas de codificación adecuadas

# Verificar y evitar divisiones por cero (si aplica)
# Agregar una pequeña cantidad (epsilon) a los denominadores para evitar divisiones por cero

# Identifiquemos las variables predictoras y la variable respuesta
X = df.drop(["Potability"], axis=1).values
Y = df["Potability"].values

# Dividimos el conjunto de datos en datos de entrenamiento y datos de prueba para evitar el overfitting
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=101)

# Lanzar y entrenar el modelo
model = sm.Logit(Y_train, X_train).fit()
print(model.summary())

Y_pred = model.predict(X_test)
Y_pred_class = (Y_pred >= 0.5).astype(int)

# Calculamos la matriz de confusión
conf_mat = confusion_matrix(Y_test, Y_pred_class)

# Mostramos la matriz de confusión en la pantalla
print("Matriz de confusión:")
print(conf_mat)

# Resto del código para generar el gráfico de la matriz de confusión, informe de clasificación y curva ROC
# ...


fig, ax = plt.subplots()
im = ax.imshow(conf_mat, cmap='Blues')

# Añadimos etiquetas para las filas y columnas de la matriz
ax.set_xticks(np.arange(len(conf_mat)))
ax.set_yticks(np.arange(len(conf_mat)))
ax.set_xticklabels(['No Potable', 'Potable'])
ax.set_yticklabels(['No Potable', 'Potable'])

# Rotamos los ticks de las etiquetas en el eje x
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Añadimos los valores de la matriz dentro de cada celda
for i in range(len(conf_mat)):
    for j in range(len(conf_mat)):
        text = ax.text(j, i, conf_mat[i, j],
                       ha="center", va="center", color="white")

# Añadimos un título y un colorbar
ax.set_title("Matriz de Confusión")
fig.colorbar(im)

# Mostramos la figura
set_window_center(plt.gcf())
plt.show()

#Informe de clasificación----------------------------------------------------------------------------
print(classification_report(Y_test, Y_pred_class))


# Calcular la curva ROC------------------------------------------------------------------------------
fpr, tpr, thresholds = roc_curve(Y_test, Y_pred)
roc_auc = auc(fpr, tpr)

# Crear el gráfico
plt.plot(fpr, tpr, color='darkorange', lw=2, label='Curva ROC (área = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('Tasa de Falsos Positivos')
plt.ylabel('Tasa de Verdaderos Positivos')
plt.title('Curva ROC del Modelo de Regresión Logística')
plt.legend(loc="lower right")
set_window_center(plt.gcf())
plt.show()

