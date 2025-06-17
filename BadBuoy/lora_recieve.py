# lora_receive.py – Listen for LoRa messages

import time
import busio
import board
import digitalio
import adafruit_rfm9x

CS = digitalio.DigitalInOut(board.D8)
RESET = digitalio.DigitalInOut(board.D25)

spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, 915.0)

print("[???] Listening for messages...")
while True:
    packet = rfm9x.receive()
    if packet is not None:
        msg = str(packet, "utf-8")
        print(f"[??] Received: {msg}")
    time.sleep(0.1)
