import time
import sys

from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics


options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.slowdowngpio = 4

options.hardware_mapping = 'adafruit-hat'

matrix = RGBMatrix(options=options)

green = graphics.Color(0, 255, 0)
graphics.DrawCircle(matrix, 15, 15, 10, green)

try:
    print("Press CTRL-C to stop.")
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    sys.exit(0)
