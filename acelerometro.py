from machine import I2C, Pin
import utime
from mpu import MPU6050 

GRAVEDAD = 9.80665  # m/s² por 1 g

i2c = I2C(0, scl=Pin(21), sda=Pin(20))
mpu = MPU6050(i2c)

while True:
    ax_g, ay_g, az_g = mpu.get_accel()    # lectura en g
    gx, gy, gz = mpu.get_gyro()           # giroscopio en °/s

    # Conversión a m/s²
    ax = ax_g * GRAVEDAD
    ay = ay_g * GRAVEDAD
    az = az_g * GRAVEDAD

    print("📌 Acelerómetro (m/s²)")
    print("Ax:", ax, " Ay:", ay, " Az:", az)

    print("📌 Giroscopio (°/s)")
    print("Gx:", gx, " Gy:", gy, " Gz:", gz)

    print("----------------------------------")
    utime.sleep(0.5)

