import utime
from machine import Pin, SPI, UART
from nrf24l01 import NRF24L01

# ---------------------------------------------------
# UART USB (CDC) — ESTE ES EL PUERTO QUE VA AL PC
# ---------------------------------------------------
# En Raspberry Pi Pico 2 W: UART(0) = USB Serial automático
uart = UART(0, baudrate=115200)

def enviar_serial(texto):
    uart.write(texto + "\n")   # Enviar al PC
    # print("UART:", texto)    # Debug opcional

# ---------------------------------------------------
# CONFIGURACIÓN DEL NRF24L01
# ---------------------------------------------------
spi = SPI(0, sck=Pin(18), mosi=Pin(19), miso=Pin(16))
csn = Pin(17, Pin.OUT)
ce  = Pin(15, Pin.OUT)

nrf = NRF24L01(spi, csn, ce, channel=100, payload_size=32)
nrf.open_rx_pipe(1, b'\xd2\xf0\xf0\xf0\xf0')
nrf.start_listening()

print("📡 Receptor PICO 2 W listo...\n")

# Variables iniciales
paquete1 = {"lat": "--", "lon": "--", "temp": "--", "hum": "--"}
paquete2 = {"ax": "--", "ay": "--", "az": "--", "gx": "--", "gy": "--", "gz": "--"}
evento_tcrt = 0

intervalo = 1
ultimo_tiempo = utime.time()

# ---------------------------------------------------
# LOOP PRINCIPAL
# ---------------------------------------------------
while True:

    # Si hay datos RF recibidos
    if nrf.any():
        data = nrf.recv()
        msg = data.decode().strip("\x00")
        print("📥 RF recibido:", msg)

        # Evento TCRT
        if msg.startswith("TCRT:"):
            evento_tcrt = int(msg.split(":")[1])
            continue

        partes = msg.split(";")

        # PAQUETE 1 → GPS + DHT
        if len(partes) == 4:
            paquete1 = {
                "lat": partes[0],
                "lon": partes[1],
                "temp": partes[2],
                "hum": partes[3]
            }

        # PAQUETE 2 → MPU6050
        elif len(partes) == 6:
            paquete2 = {
                "ax": partes[0],
                "ay": partes[1],
                "az": partes[2],
                "gx": partes[3],
                "gy": partes[4],
                "gz": partes[5]
            }

    # Enviar mega-paquete cada 1 segundo
    if utime.time() - ultimo_tiempo >= intervalo:
        ultimo_tiempo = utime.time()

        mega = "{};{};{};{};{};{};{};{};{};{};{}".format(
            paquete1["lat"], paquete1["lon"], paquete1["temp"], paquete1["hum"],
            paquete2["ax"], paquete2["ay"], paquete2["az"],
            paquete2["gx"], paquete2["gy"], paquete2["gz"],
            evento_tcrt
        )

        enviar_serial(mega)        # ← ENVÍO POR USB
        evento_tcrt = 0            # reset
        print("📤 Enviado USB:", mega)

    utime.sleep(0.05)
