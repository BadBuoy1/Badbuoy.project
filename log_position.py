import serial
from datetime import datetime

with serial.Serial("/dev/serial0", 9600, timeout=1) as ser:
    with open("gps_log.csv", "a") as log:
        while True:
            line = ser.readline().decode("ascii", errors="ignore")
            if line.startswith("$GPGGA"):
                now = datetime.utcnow().isoformat()
                log.write(f"{now},{line.strip()}\n")
                print(f"[{now}] {line.strip()}")
