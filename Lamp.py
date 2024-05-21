import time
import board
import neopixel
from digitalio import DigitalInOut, Direction, Pull
import analogio
import math

pixel_pin = board.D2
num_pixels = 16

switchpin1 = board.D3
switch1 = DigitalInOut(switchpin1)
switch1.direction = Direction.INPUT
switch1.pull = Pull.UP

switchpin2 = board.D1
switch2 = DigitalInOut(switchpin2)
switch2.direction = Direction.INPUT
switch2.pull = Pull.UP

buttonpin = board.D0
button = DigitalInOut(buttonpin)
button.direction = Direction.INPUT
button.pull = Pull.UP

potpin = board.A4  #pin 0 is Analog input 2
pot = analogio.AnalogIn(potpin)

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

OFF = (0,0,0)

MINT = (0, 255, 191)
TURQUOISE = (3, 252, 227)
BLUE1 = (3, 152, 252)
NAVY = (4, 64, 194)
PURPLE = (214, 120, 255)

colors = [MINT, TURQUOISE, BLUE1, NAVY, PURPLE]
colornum = 0
color = OFF
colorlist = []

fade = 16
fadeup = False

while True:
    #print(math.sqrt(pot.value)-1)
    if switch1.value:
        #print(1)
        if not button.value:
            colornum += 1
            if colornum > len(colors):
                colornum = 0
        if colornum == len(colors):
            #rgb
            pass
        else:
            color = colors[colornum]
        if switch2.value:
            colorlist = list(color)
            for x in range(len(colorlist)):
                num = colorlist[x]
                num *= fade/16
                colorlist[x] = int(num)
            color = tuple(colorlist)
            if fadeup:
                fade += 1
            else:
                fade -= 1
            if fade == 0:
                fadeup = True
            elif fade == 16:
                fadeup = False
        else:
            #potentiometer
            pass
    else:
        color = OFF
        #print(0)

    pixels.fill(color)
    pixels.show()
