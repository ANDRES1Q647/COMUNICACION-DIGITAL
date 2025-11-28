from machine import Pin, PWM, ADC
import time

# Configuración del servo (PWM)
servo = PWM(Pin(15))
servo.freq(50)  # Frecuencia estándar para servos

# Configuración del joystick
joystick_x = ADC(Pin(26))  # Eje X

# Función para mover el servo
def mover_servo(angulo):
    # Mapeo de 0°–180° a ciclo de trabajo (duty_u16)
    # Ajusta los valores si tu servo no llega bien a los extremos
    min_duty = 1638   # ~0.5 ms
    max_duty = 8192   # ~2.5 ms
    duty = int(min_duty + (angulo / 180) * (max_duty - min_duty))
    servo.duty_u16(duty)

# Ángulo central
angulo_centro = 90

while True:
    # Leer valor del joystick (0 a 65535)
    valor = joystick_x.read_u16()

    # Mapeo: joystick 0–65535 a servo 45–135 grados
    angulo = int((valor / 65535) * 90 + 45)

    # Si el servo gira al revés, invierte los límites:
    # angulo = int((1 - valor / 65535) * 90 + 45)

    mover_servo(angulo)

    print("Joystick:", valor, "  Servo:", angulo)
    time.sleep(0.05)
