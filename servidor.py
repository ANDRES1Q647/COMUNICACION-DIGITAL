import serial
import asyncio
import websockets

# 🔧 CAMBIAR SEGÚN TU PC:
# Windows: "COM3"
# Linux:   "/dev/ttyACM0"
# macOS:   "/dev/cu.usbmodem1101"
SERIAL_PORT = "COM14"
BAUD = 115200

async def transmitir(websocket, path):
    print(f"🔌 Abriendo puerto serial {SERIAL_PORT} ...")
    ser = serial.Serial(SERIAL_PORT, BAUD)
    print("🟢 RS232 listo. Enviando datos al navegador...")

    while True:
        try: 
            linea = ser.readline().decode(errors="ignore").strip()
            if linea:
                await websocket.send(linea)
        except:
            pass

start_server = websockets.serve(transmitir, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
print("🟢 WebSocket activo en ws://localhost:8765")
asyncio.get_event_loop().run_forever()
