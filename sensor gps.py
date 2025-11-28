from machine import UART, Pin
import time

gps = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

# Variables para mantener últimos valores válidos
ultima_fecha = "--/--/----"
ultima_hora = "--:--:--"
ultima_lat = "----"
ultima_lon = "----"
ultimo_sat = "0"

def convertir_a_decimal(valor, direccion):
    if valor == "":
        return None
    grados = int(valor[:2])
    minutos = float(valor[2:])
    decimal = grados + minutos / 60
    if direccion in ["S", "W"]:
        decimal *= -1
    return decimal

def convertir_hora_local(hora_utc):
    if len(hora_utc) < 6:
        return "--:--:--"
    hh = int(hora_utc[0:2]) - 5  # UTC -5
    if hh < 0:
        hh += 24
    mm = hora_utc[2:4]
    ss = hora_utc[4:6]
    return f"{hh:02d}:{mm}:{ss}"

def convertir_fecha(fecha_gps):
    if len(fecha_gps) != 6:
        return "--/--/----"
    dd = fecha_gps[0:2]
    mm = fecha_gps[2:4]
    yyyy = 2000 + int(fecha_gps[4:6])
    return f"{dd}/{mm}/{yyyy}"

while True:
    if gps.any():
        linea = gps.readline()
        try:
            linea = linea.decode()

            # --- Datos de ubicación (RMC) ---
            if linea.startswith("$GPRMC"):
                datos = linea.split(",")

                estado = datos[2]
                if estado == "A":  # Datos válidos
                    ultima_hora = convertir_hora_local(datos[1])
                    ultima_lat = convertir_a_decimal(datos[3], datos[4])
                    ultima_lon = convertir_a_decimal(datos[5], datos[6])
                    ultima_fecha = convertir_fecha(datos[9])

            # --- Número de satélites (GGA) ---
            if linea.startswith("$GPGGA"):
                datos = linea.split(",")
                if len(datos) > 7:
                    ultimo_sat = datos[7]

            # --- Mostrar SIEMPRE todos los datos ---
            print("📅 Fecha:", ultima_fecha)
            print("🕒 Hora local:", ultima_hora)
            print("🌐 Latitud :", ultima_lat)
            print("🌐 Longitud:", ultima_lon)
            print("🛰 Satélites:", ultimo_sat)
            print("-------------------------")

        except Exception as e:
            print("Error:", e)

    time.sleep(0.2)