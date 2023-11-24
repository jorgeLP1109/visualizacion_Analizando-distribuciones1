import matplotlib.pyplot as plt
import pandas as pd

datos = pd.read_csv('datos.csv')

# Graficar la distribución de edades con un histograma
plt.figure(figsize=(10, 6))
plt.hist(datos['edad'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribución de Edades')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()

# Graficar histogramas agrupados por hombre y mujer
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Cantidad de anémicos
axs[0, 0].hist(datos[datos['sexo'] == 'Hombre']['anemico'], bins=[-0.5, 0.5, 1.5], color='blue', alpha=0.7, label='Hombre', rwidth=0.8)
axs[0, 0].hist(datos[datos['sexo'] == 'Mujer']['anemico'], bins=[-0.5, 0.5, 1.5], color='pink', alpha=0.7, label='Mujer', rwidth=0.8)
axs[0, 0].set_title('Cantidad de Anémicos')
axs[0, 0].set_xticks([0, 1])
axs[0, 0].set_xticklabels(['No Anémico', 'Anémico'])
axs[0, 0].legend()

# Cantidad de diabéticos
axs[0, 1].hist(datos[datos['sexo'] == 'Hombre']['diabetico'], bins=[-0.5, 0.5, 1.5], color='blue', alpha=0.7, label='Hombre', rwidth=0.8)
axs[0, 1].hist(datos[datos['sexo'] == 'Mujer']['diabetico'], bins=[-0.5, 0.5, 1.5], color='pink', alpha=0.7, label='Mujer', rwidth=0.8)
axs[0, 1].set_title('Cantidad de Diabéticos')
axs[0, 1].set_xticks([0, 1])
axs[0, 1].set_xticklabels(['No Diabético', 'Diabético'])
axs[0, 1].legend()

# Cantidad de fumadores
axs[1, 0].hist(datos[datos['sexo'] == 'Hombre']['fumador'], bins=[-0.5, 0.5, 1.5], color='blue', alpha=0.7, label='Hombre', rwidth=0.8)
axs[1, 0].hist(datos[datos['sexo'] == 'Mujer']['fumador'], bins=[-0.5, 0.5, 1.5], color='pink', alpha=0.7, label='Mujer', rwidth=0.8)
axs[1, 0].set_title('Cantidad de Fumadores')
axs[1, 0].set_xticks([0, 1])
axs[1, 0].set_xticklabels(['No Fumador', 'Fumador'])
axs[1, 0].legend()

# Cantidad de muertos
axs[1, 1].hist(datos[datos['sexo'] == 'Hombre']['muerto'], bins=[-0.5, 0.5, 1.5], color='blue', alpha=0.7, label='Hombre', rwidth=0.8)
axs[1, 1].hist(datos[datos['sexo'] == 'Mujer']['muerto'], bins=[-0.5, 0.5, 1.5], color='pink', alpha=0.7, label='Mujer', rwidth=0.8)
axs[1, 1].set_title('Cantidad de Muertos')
axs[1, 1].set_xticks([0, 1])
axs[1, 1].set_xticklabels(['No Muerto', 'Muerto'])
axs[1, 1].legend()

plt.tight_layout()
plt.show()
