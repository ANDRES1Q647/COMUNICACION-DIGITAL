import machine
import utime
from machine import Pin, UART

# LED integrado
led = Pin("LED", Pin.OUT)

# UART0 en GP0 (TX) y GP1 (RX)
uart = UART(
    0,
    baudrate=9600,
    bits=8,
    parity=None,
    stop=1,
    tx=Pin(0),
    rx=Pin(1)
)

print("Esperando datos por UART...\n")

while True:
    # ¿Hay datos disponibles en el buffer?
    if uart.any():
        # Leer todo lo disponible
        data = uart.read()
        if data:
            # Encender/apagar LED como indicador de recepción
            led.toggle()
            try:
                # Decodificar a texto (asumiendo ASCII/UTF-8)
                texto = data.decode()
            except:
                # Si no se puede decodificar, lo muestra como bytes
                texto = str(data)
            # Imprimir sin salto extra de línea
            print(texto, end="")
    # Pequeña pausa para no saturar la CPU
    utime.sleep(0.01)
