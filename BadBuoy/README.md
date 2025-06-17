# ?? BadBuoy Project

**BadBuoy** is an open-source DIY mesh buoy project built for:

- Coastal surveillance
- GPS spoofing detection
- Ocean research
- Emergency relay signaling

Powered by Raspberry Pi Zero 2 W + LoRa + GPS. Modular. Cheap. Deployable.

---

## Project Overview

Each buoy:
- Reads GPS position via `gpsd`
- Sends messages via RFM95W LoRa module (915 MHz)
- Runs on battery power, optionally solar in future

---

## Hardware

Each PoC unit includes:

- Raspberry Pi Zero 2 W
- NEO-6M GPS module
- Adafruit RFM95W LoRa module (U.FL + SMA antenna)
- Breadboard & jumper wires
- USB power bank or LiPo battery
- DIY boat hull / cannibalize an RC boat , motors can vary 

---

##  Quick Start

### 1. Clone this repo

```bash
git clone https://github.com/BadBuoy1/Badbuoy.project.git badbuoy
cd badbuoy
