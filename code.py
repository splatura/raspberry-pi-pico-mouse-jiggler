import time
import usb_hid
from adafruit_hid.mouse import Mouse
import board
import neopixel
import random

# Define the NeoPixel pin to suit the board in use
NEOPIXEL=board.GP16

mouse = Mouse(usb_hid.devices)
pixels = neopixel.NeoPixel(NEOPIXEL, 1, brightness=0.3, auto_write=False)
pixels[0] = (10, 0, 0)


#led = digitalio.DigitalInOut(board.GP16)
#led.direction = digitalio.Direction.OUTPUT

def generate_random_numbers(start=0.2, end=5.7):
    # Generate two random floating-point numbers between start and end
    random_number1 = random.uniform(start, end)
    random_number2 = random.uniform(start, end)
    return [random_number1, random_number2]

start_sleeptime = generate_random_numbers(4.3,6)
print(f"First sleep time is :{start_sleeptime}")

time.sleep(start_sleeptime[0])

while True:
	pixels[0] = (10, 0, 0)
	pixels.show()
	randomMove = generate_random_numbers()
	print(f"randomMove X is :{randomMove[0]}")
	print(f"randomMove Y is :{randomMove[1]}")
	# Make the X and Y mouse movements integers
	randomMove[0] = round(randomMove[0]*2)
	randomMove[1] = round(randomMove[1]*2)
	mouse.move(x=randomMove[0],y=randomMove[1])
	sleepTime = generate_random_numbers(0.1,20.6)
	print(f"sleepTime is :{sleepTime[0]}")
	time.sleep(sleepTime[0])

	# Move back to original position
	pixels[0] = (0, 0, 0)
	pixels.show()
	mouse.move(x=-randomMove[0],y=-randomMove[1])
	sleepTime = generate_random_numbers(0.1,20.6)
	time.sleep(sleepTime[0])
	print(f"sleepTime is :{sleepTime[0]}")
