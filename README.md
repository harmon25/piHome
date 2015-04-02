#piHome
Home Automation Scripts for small linux based SoC (Raspberry Pi)

## Dependencies
- Hardware
 - Raspberry Pi (Multiple)
 - RGB LED
 - DS18B20 Temp Sensor
 - SSD1306 OLED 128x64
- Software Libraries
 - RPI.GPIO Library
 - pi-blaster - PWM on the Raspberry pi - done properly
 - Adafruit SSD1306 Python Library
 - w1thermsensor Python Library

```shell
sudo apt-get install python git python-dev python-pip python-imaging
sudo pip install python-rpi.gpio 
git clone https://github.com/adafruit/Adafruit_Python_SSD1306
git clone https://github.com/timofurrer/w1thermsensor
git clone https://github.com/sarfata/pi-blaster

```