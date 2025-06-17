# main.py – Main loop for buoy behavior

from gps_test import get_gps_data
from lora_send import send_message
import time

while True:
    gps_data = get_gps_data()
    if gps_data:
        print(f"Sending GPS data: {gps_data}")
        send_message(gps_data)
    else:
        print("Waiting for GPS fix...")
    time.sleep(10)
