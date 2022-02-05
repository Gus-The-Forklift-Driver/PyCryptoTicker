import time
import sys

from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics

# options for the display
options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.gpio_slowdown = 4  # less bleeding with py 4
options.hardware_mapping = 'adafruit-hat'

font = graphics.Font()
font.LoadFont("7x13.bdf")

# initialize matrix
matrix = RGBMatrix(options=options)

green = graphics.Color(0, 255, 0)
graphics.DrawCircle(matrix, 15, 15, 10, green)
matrix.Fill(20, 0, 0)


def displayTicker(currency='BTC', change=20, currentPrice=35904, fiat='$'):
    graphics.DrawText(matrix, font, 0, 13, green, currency)
    graphics.DrawText(matrix, font, 0, 26, green, str(currentPrice))
    if change > 0:
        graphics.DrawText(matrix, font, 20, 26, green, "▲")


displayTicker()


try:
    print("Press CTRL-C to stop.")
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    sys.exit(0)
