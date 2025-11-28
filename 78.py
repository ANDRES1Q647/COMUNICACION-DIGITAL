from machine import Pin, SPI
from nrf24l01 import NRF24L01
import utime

spi = SPI(1, sck=Pin(10), mosi=Pin(11), miso=Pin(12))
csn = Pin(13, Pin.OUT)
ce = Pin(9, Pin.OUT)

radio = NRF24L01(spi, csn, ce)
pipes = (b"1Node", b"2Node")
radio.open_tx_pipe(pipes[0])
radio.open_rx_pipe(1, pipes[1])
radio.stop_listening()

while True:
    msg = b"Hola"
    radio.send(msg)
    print("📤 Enviado:", msg)
    utime.sleep(1)
