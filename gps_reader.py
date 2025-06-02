import serial

# Open serial connection to GPS module
with serial.Serial("/dev/serial0", baudrate=9600, timeout=1) as ser:
    while True:
        line = ser.readline().decode("ascii", errors="replace").strip()
        if line.startswith("$GPGGA") or line.startswith("$GPRMC"):
            print(line)

