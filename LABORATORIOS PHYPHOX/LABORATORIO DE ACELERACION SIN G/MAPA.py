import pandas as pd
import folium
import webbrowser


df = pd.read_csv("Raw Data-1.csv", sep='\t', quotechar='"')

df = df.dropna(subset=['Latitude (°)', 'Longitude (°)'])

start_lat = df['Latitude (°)'].iloc[0]
start_lon = df['Longitude (°)'].iloc[0]

mapa = folium.Map(location=[start_lat, start_lon], zoom_start=18)

coordenadas = list(zip(df['Latitude (°)'], df['Longitude (°)']))

folium.PolyLine(coordenadas, color='blue').add_to(mapa)

for lat, lon in coordenadas:
    folium.CircleMarker(location=[lat, lon], radius=3, color='red').add_to(mapa)

mapa_path = 'ruta_gps_phyphox.html'
mapa.save(mapa_path)
print(f"Mapa guardado como {mapa_path}")

webbrowser.open(mapa_path)
