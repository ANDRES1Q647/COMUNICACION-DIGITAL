import matplotlib.pyplot as plt
import pandas as pd


P = pd.read_csv('Raw Data-1.csv', sep='\t')
P.columns = P.columns.str.strip().str.replace('"', '', regex=False)


t = P['Time (s)']

# 1. LATITUD y LONGITUD
plt.figure()
plt.subplot(2,1,1)
plt.plot(t, P['Latitude (°)'], color='blue')
plt.title('LATITUD VS TIEMPO')
plt.xlabel('Tiempo(s)')
plt.ylabel('Latitud(°)')
plt.grid(True, linewidth=1.5)
plt.tight_layout()

plt.subplot(2,1,2)
plt.plot(t, P['Longitude (°)'], color='black')
plt.title('LONGITUD VS TIEMPO')
plt.xlabel('Tiempo(s)')
plt.ylabel('Longitud(°)')
plt.grid(True, linewidth=1.5)
plt.tight_layout()

# 2. ALTITUD y ALTITUD WGS84
plt.figure()
plt.subplot(2,1,1)
plt.plot(t, P['Altitude (m)'], color='red')
plt.title('ALTITUD VS TIEMPO')
plt.xlabel('Tiempo(s)')
plt.ylabel('Altitud(m)')
plt.grid(True, linewidth=1.5)
plt.tight_layout()

plt.subplot(2,1,2)
plt.plot(t, P['Altitude WGS84 (m)'], color='green')
plt.title('ALTITUD VS TIEMPO')
plt.xlabel('Tiempo(s)')
plt.ylabel('Altitud(w)')
plt.grid(True, linewidth=1.5)
plt.tight_layout()

# 3. VELOCIDAD y DIRECCIÓN
plt.figure()
plt.subplot(2,1,1)
plt.plot(t, P['Speed (m/s)'], color='blue')
plt.title('VELOCIDAD VS TIEMPO')
plt.xlabel('Tiempo(s)')
plt.ylabel('Velocidad(m/s)')
plt.grid(True, linewidth=1.5)
plt.tight_layout()

plt.subplot(2,1,2)
plt.plot(t, P['Direction (°)'], color='red')
plt.title('DIRECCION VS TIEMPO')
plt.xlabel('Tiempo(s)')
plt.ylabel('Direccion(º)')
plt.grid(True, linewidth=1.5)
plt.tight_layout()

# 4. DISTANCIA y HORIZONTAL ACCURACY
plt.figure()
plt.subplot(2,1,1)
plt.plot(t, P['Distance (km)'], color='magenta')
plt.title('DISTANCIA VS TIEMPO')
plt.xlabel('Tiempo(s)')
plt.ylabel('Distancia(KM)')
plt.grid(True, linewidth=1.5)
plt.tight_layout()

plt.subplot(2,1,2)
plt.plot(t, P['Horizontal Accuracy (m)'], color='cyan')
plt.title('Horizontal VS TIEMPO')
plt.xlabel('Tiempo(s)')
plt.ylabel('Horizontal(m)')
plt.grid(True, linewidth=1.5)
plt.tight_layout()

# 5. VERTICAL ACCURACY y SATÉLITES
plt.figure()
plt.subplot(2,1,1)
plt.plot(t, P['Vertical Accuracy (m)'], color='blue')
plt.title('VERTICAL VS TIEMPO')
plt.xlabel('Tiempo(s)')
plt.ylabel('Vertical(m)')
plt.grid(True, linewidth=1.5)
plt.tight_layout()

plt.subplot(2,1,2)
plt.plot(t, P['Satellites'], color='blue')
plt.title('SATÉLITES VS TIEMPO')
plt.xlabel('Tiempo(s)')
plt.ylabel('Satélites')
plt.grid(True, linewidth=1.5)
plt.tight_layout()

plt.show()
