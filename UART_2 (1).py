import machine
import utime
from machine import Pin,UART
led = machine.Pin("LED", machine.Pin.OUT)
uart = UART(0, baudrate=9600,bits=8,parity=None, tx=Pin(0), rx=Pin(1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        )
while True:
 led.on()
 uart.write("Telecomunicaciones_UMNG_2025")
 utime.sleep(1)
 led.off()
 utime.sleep(1)
 
 
 



 