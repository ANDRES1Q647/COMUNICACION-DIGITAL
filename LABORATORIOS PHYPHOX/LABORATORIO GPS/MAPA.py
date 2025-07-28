import pandas as pd
import folium
import webbrowser

# Leer el CSV con separador de tabulación y comillas
df = pd.read_csv("Raw Data-1.csv", sep='\t', quotechar='"')

# Eliminar filas sin coordenadas
df = df.dropna(subset=['Latitude (°)', 'Longitude (°)'])

# Obtener coordenadas iniciales para centrar el mapa
start_lat = df['Latitude (°)'].iloc[0]
start_lon = df['Longitude (°)'].iloc[0]

# Crear mapa centrado en el primer punto
mapa = folium.Map(location=[start_lat, start_lon], zoom_start=18)

# Extraer coordenadas como lista de tuplas
coordenadas = list(zip(df['Latitude (°)'], df['Longitude (°)']))

# Dibujar la ruta
folium.PolyLine(coordenadas, color='blue').add_to(mapa)

# Añadir puntos individuales opcionalmente
for lat, lon in coordenadas:
    folium.CircleMarker(location=[lat, lon], radius=3, color='red').add_to(mapa)

# Guardar mapa
mapa_path = 'ruta_gps_phyphox.html'
mapa.save(mapa_path)
print(f"Mapa guardado como {mapa_path}")

webbrowser.open(mapa_path)
