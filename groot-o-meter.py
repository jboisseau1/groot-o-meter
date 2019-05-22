import time
import datetime
import board
from board import SCL, SDA
import busio
import neopixel
from adafruit_seesaw.seesaw import Seesaw

#port sensor setup
i2c_bus = busio.I2C(SCL, SDA) #GPIO
ss = Seesaw(i2c_bus, addr=0x36) #pot sensor

# NeoPixel setup
pixel_pin = board.D18 #GPIO
num_pixels = 30
ORDER = neopixel.GRB


# change brightness level very low if time is between 10pm and 6am EST
brightness_level = 0.5
if night_time():
    brightness_level = 0.01


pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=brightness_level, auto_write=False, pixel_order=ORDER)

# checks if it is night time currently
# returns true if night time; false otherwise
def night_time():
    start = datetime.time(22, 0, 0) #10pm
    end = datetime.time(6, 0, 0) #6am
    current = datetime.time(datetime.datetime.now().hour,datetime.datetime.now().minute,datetime.datetime.now().second)

    if start <= end:
        return start <= current <= end
    else:
        return start <= current or current <= end


def display_moisture_level():
    # read moisture level through capacitive touch pad
    wetness = ss.moisture_read()
    print("Moisture level: " + str(wetness))

    #flashes red when groot needs water
    while wetness < 320:
        print("VERY LOW  moisture: " + str(wetness))
        pixels.fill((255, 0, 0)) #full red - very dry
        pixels.show()
        time.sleep(.75)
        pixels.fill((0,0,0)) #off
        pixels.show()
        time.sleep(.75)
        wetness = ss.moisture_read()

    if wetness > 321 and wetness < 600:
        green_val = round(255*((wetness-321)/(600-321)))

        print("351-500: G"+str(green_val))
        pixels.fill((255, green_val, 0)) #from red to yellow based on sensor
        pixels.show()

    if wetness > 601 and wetness < 1000:
        red_val = 255-(round(255*((wetness-601)/(1000-601))))

        print("701-1000: R" + str(red_val))
        pixels.fill((red_val,255, 0)) #from yellow to green based on sensor
        pixels.show()

    if wetness > 1001:
        pixels.fill((0, 255, 0)) #full green - very wet
        pixels.show()


while True:
    display_moisture_level()
    time.sleep(.5)
