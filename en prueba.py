from machine import Pin, I2C, SPI
from nrf24l01 import NRF24L01
from mpu6050 import MPU6050
import utime

# --- Inicialización del acelerómetro MPU6050 ---
i2c_mpu = I2C(0, scl=Pin(9), sda=Pin(8))
mpu = MPU6050(i2c_mpu)

# --- Configuración del módulo NRF24L01 ---
# SPI: asegúrate de usar los pines correctos según tu microcontrolador
spi = SPI(0, baudrate=4000000, polarity=0, phase=0,
          sck=Pin(18), mosi=Pin(19), miso=Pin(16))
csn = Pin(17, Pin.OUT, value=1)
ce = Pin(20, Pin.OUT, value=0)

# Direcciones de los nodos (5 bytes cada una)
pipes = (b"1Node", b"2Node")

# Inicialización del módulo NRF24L01
nrf = NRF24L01(spi, csn, ce, channel=76, payload_size=32)

# Configurar como transmisor (TX)
nrf.open_tx_pipe(pipes[1])  # Dirección destino (receptor)
nrf.open_rx_pipe(0, pipes[0])  # Canal de retorno para ACK (opcional)

print("🚀 Transmisor NRF24L01 listo...")

# --- Bucle principal ---
while True:
    # Obtener valores del acelerómetro
    values = mpu.get_accel_only()
    ax = round(values['AcX'], 2)
    ay = round(values['AcY'], 2)
    az = round(values['AcZ'], 2)

    # Crear mensaje a enviar
    msg = f"{ax},{ay},{az}"

    try:
        nrf.send(msg.encode('utf-8'))
        print("📤 Enviado:", msg)
    except OSError as e:
        print("⚠️ Error al enviar:", e)

    utime.sleep(0.5)
