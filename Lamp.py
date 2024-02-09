import time
import board
import neopixel
from digitalio import DigitalInOut, Direction, Pull

pixel_pin = board.D2
num_pixels = 16

switchpin1 = board.D3
switch1 = DigitalInOut(switchpin1)
switch1.direction = Direction.INPUT
switch1.pull = Pull.UP

switchpin2 = board.D4
switch2 = DigitalInOut(switchpin1)
switch2.direction = Direction.INPUT
switch2.pull = Pull.UP

buttonpin = board.D5
button = DigitalInOut(buttonpin)
button.direction = Direction.INPUT
button.pull = Pull.UP

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

OFF = (0,0,0)

colors = []
colornum = 0
color = OFF

fade = 16
fadeup = False

while True:
    if switch1.value:
        if not button.value:
            colornum += 1
            if colornum > len(colors):
                colornum = 0
        if colornum == len(colors):
            #rgb
        else:
            color = colors[colornum]
        if switch2.value:
            for x in range(len(color)):
                color[x] *= fade/16
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

    pixels.fill(color)
    pixels.show()
