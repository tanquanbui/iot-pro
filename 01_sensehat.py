from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear(255, 255, 255)

sense.low_light = True
time.sleep(2)

sense.low_light = False
time.sleep(2)

sense.clear()
