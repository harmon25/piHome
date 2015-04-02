```
          _ _   _                      
    _ __ (_| | | | ___  _ __ ___   ___ 
   | '_ \| | |_| |/ _ \| '_ ` _ \ / _ \
   | |_) | |  _  | (_) | | | | | |  __/
   | .__/|_|_| |_|\___/|_| |_| |_|\___|
   |_|                                

Home Automation Scripts for small linux based SoC (Raspberry Pi)
```
piHome
=======

## Dependencies
### Hardware
 - Raspberry Pi(s) (Multiple)
 - Main Server (Not a Pi, but could be a Pi...)
 - Relay Module(s)
  - http://www.dx.com/p/jtron-1-channel-opto-isolated-relay-module-isolation-module-black-270934
 - RGB LED(s)
 - DS18B20 Temp Sensor(s)
 - SSD1306 OLED 128x64(s)

### Software Libraries
 - python3
 - MySQL
 - Flask
 - RPI.GPIO Library
 - pi-blaster - PWM on the Raspberry pi - done properly
 - Adafruit SSD1306 Python Library
 - w1thermsensor Python Library

## Client Sensor
```shell
sudo apt-get install python3 git python3-dev python3-pip mysql-client
sudo pip-3.2 install python-rpi.gpio PyMySQL
git clone https://github.com/timofurrer/w1thermsensor
git clone https://github.com/sarfata/pi-blaster
```
## Client Switch with Display
```shell
sudo apt-get install python3 git python3-dev python3-pip python3-imaging
git clone https://github.com/adafruit/Adafruit_Python_SSD1306
```

## Server
```shell
sudo apt-get install python3 git python3-dev python3-pip python3-imaging mysql-server
```