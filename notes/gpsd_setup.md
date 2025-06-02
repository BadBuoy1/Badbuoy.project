# GPSD Setup (Manual Start)

1. Disable socket-based auto-start:
```bash
sudo systemctl stop gpsd.socket
sudo systemctl disable gpsd.socket

#manually launch gpsd:
sudo gpsd /dev/serial0 -F /var/run/gpsd.sock
#verify
cgps
# or
gpsmon /dev/serial0

#the cgps may not populate unless you are close to a window or open area, thick walls or metal roofs can have an effect
