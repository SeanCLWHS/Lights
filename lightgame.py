import time
import board
import neopixel
from digitalio import DigitalInOut, Direction, Pull

pixel_pin = board.D2   #the ring data is connected to this pin
num_pixels = 16   #number of leds pixels on the ring

button_pin = board.D3

switch = DigitalInOut(button_pin)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

pixel_num = 0

level = 0
speed = 0.25
win = False
done = False

RED = (255, 0, 0) #RGB
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255,255,255)
OFF = (0,0,0)

def Reset():
    for x in range(15):
        pixels[x] = OFF
    pixels[15]=RED
    pixels.show()
    time.sleep(1)
    pixel_num = 0
    
    #win = false

def ButtonPress():
    return switch.value

while True:
    speed = 0.25
    for level in range(16):
        Reset()
        for pixel_num in range(16):
            pixels[pixel_num]=GREEN
            pixels.show()
            time.sleep(speed)
            if not ButtonPress():
                if pixel_num == 15:
                    win = True
                else:
                    break
        if win:
            if level == 15:
                pixels.fill(OFF)
                for x in range(level+1):
                    pixels[x] = CYAN
                    pixels.show()
                    time.sleep(0.5)
                while ButtonPress():
                    pass
                break
            else:
                time.sleep(1)
                speed *=0.75
        else:
            pixels.fill(RED)
            pixels.show()
            time.sleep(2.5)
            pixels.fill(OFF)
            for x in range(level+1):
                pixels[x] = CYAN
                pixels.show()
                time.sleep(0.5)
            while ButtonPress():
                pass
            break
            
        win = False
