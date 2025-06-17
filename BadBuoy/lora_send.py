# lora_send.py – Send a LoRa message

import time
import busio
import board
import digitalio
import adafruit_rfm9x

CS = digitalio.DigitalInOut(board.D8)
RESET = digitalio.DigitalInOut(board.D25)

spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, 915.0)

def send_message(message):
    rfm9x.send(bytes(message, "utf-8"))
    print(f"[??] Sent: {message}")

if __name__ == "__main__":
    send_message("BadBuoy - BadBuoy-whatch'a gon-na do?!")
