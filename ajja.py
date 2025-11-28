import pandas as pd
import matplotlib.pyplot as plt


L = pd.read_csv('Raw Data.csv', sep='\t')  


L.columns = L.columns.str.strip().str.replace('"', '', regex=False)


print("Columnas detectadas:", L.columns.tolist())


t = L['Time (s)']
x1 = L['Linear Acceleration x (m/s^2)']
y1 = L['Linear Acceleration y (m/s^2)']
z1 = L['Linear Acceleration z (m/s^2)']
a1 = L['Absolute acceleration (m/s^2)']


plt.figure(figsize=(10, 8))

plt.subplot(4, 1, 1)
plt.plot(t, x1, color='red')
plt.title('TIEMPO (S) VS ACELERACIÓN EN CADA CASO')
plt.xlabel('Tiempo (s)')
plt.ylabel('Ace en X')

plt.subplot(4, 1, 2)
plt.plot(t, y1, color='green')
plt.xlabel('Tiempo (s)')
plt.ylabel('Ace en Y')

plt.subplot(4, 1, 3)
plt.plot(t, z1, color='black')
plt.xlabel('Tiempo (s)')
plt.ylabel('Ace en Z')

plt.subplot(4, 1, 4)
plt.plot(t, a1, color='blue')
plt.xlabel('Tiempo (s)')
plt.ylabel('Ace ABS')

plt.tight_layout()
plt.show()

