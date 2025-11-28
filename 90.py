from machine import Pin, I2C, SPI
from nrf24l01 import NRF24L01
from mpu6050 import MPU6050
import utime

# --- Configuración del MPU6050 (I2C) ---
i2c = I2C(1, scl=Pin(7), sda=Pin(6))
sensor = MPU6050(i2c)

# --- Configuración del NRF24L01 (SPI) ---
spi = SPI(1, sck=Pin(10), mosi=Pin(11), miso=Pin(12))
csn = Pin(13, Pin.OUT)
ce = Pin(9, Pin.OUT)

radio = NRF24L01(spi, csn, ce, payload_size=32)
pipes = (b"1Node", b"2Node")

radio.open_tx_pipe(pipes[0])   # Transmisor -> Receptor
radio.open_rx_pipe(1, pipes[1])
radio.stop_listening()         # Modo transmisión

print("🚀 Transmisor iniciado (MPU6050 + NRF24L01)")

# --- Bucle principal ---
while True:
    try:
        # Leer valores del acelerómetro
        vals = sensor.get_values()
        ax = vals["AcX"]
        ay = vals["AcY"]
        az = vals["AcZ"]

        # Escalar a 'g' para reducir tamaño
        ax_g = ax / 16384
        ay_g = ay / 16384
        az_g = az / 16384

        # Formatear y enviar
        data = "{:.2f},{:.2f},{:.2f}".format(ax_g, ay_g, az_g)
        radio.send(data.encode())

        print("📤 Enviado:", data)
        utime.sleep(0.05)  # Frecuencia de actualización ~20Hz

    except OSError:
        print("⚠️ Error I2C con MPU6050. Reintentando...")
        utime.sleep(1)
    except Exception as e:
        print("⚠️ Error general:", e)
        utime.sleep(1)
