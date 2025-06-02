# GPS Wiring Guide: Bad Buoys

Module: GY-NEO6MV2  
Connection: Raspberry Pi Zero 2 W  
Interface: UART via GPIO

| GPS Pin | Connects To Pi Pin | Pin # | Function |
|---------|---------------------|--------|----------|
| VCC     | 5V Power            | Pin 2 or 4 | Power |
| GND     | Ground              | Pin 6     | Ground |
| TX      | GPIO15 (RXD)        | Pin 10    | Serial Receive |
| RX      | (Not used)          | —        | — |

*Note:* LED may blink only after GPS fix is acquired - that includes no light when powered on and functioning -
