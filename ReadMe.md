# Groot's hydration display

Takes sensor data from Adafruit's soil hydration sensor to display hydration level on NeoPixel LEDs. Designed to run on a Raspberry Pi. The lights are automaticly dimmed between 10pm and 6am.

## Run:

`sudo python3 groot-o-meter.py`

## Raspberry Pi Setup:

To run the script on start up do the following:

`sudo nano /etc/rc.local`

At the bottom of the file just before `exit 0` add the absolute path to the `groot-o-meter.py` file.

`sudo reboot` to test your handy work.

## Python Libraries:

`sudo pip3 install adafruit-circuitpython-seesaw`

`sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel`

## Hardware:

Adafruit NeoPixel LED Strip - https://www.adafruit.com/product/3919

Adafruit STEMMA Soil Sensor - https://www.adafruit.com/product/4026

Raspberry Pi - https://www.adafruit.com/product/3055
