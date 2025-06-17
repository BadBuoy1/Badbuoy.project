# test_all.py � Optional test runner

from gps_test import get_gps_data
from lora_send import send_message

print("[??] Running full buoy test...")

gps = get_gps_data()
if gps:
    print(f"[??] GPS fix: {gps}")
    send_message(f"GPS: {gps}")
else:
    print("[??] No GPS fix.")
