import time
import sys

from secret import ReadAndWrite
from binance.client import Client
from itertools import cycle

from settings import settings

from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics

client = Client(ReadAndWrite['Api Key'], ReadAndWrite['Secret Key'])

# options for the display
options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.gpio_slowdown = 3  # less bleeding with the pi 4
options.hardware_mapping = 'adafruit-hat'
options.brightness = 50

font_medium = graphics.Font()
font_medium.LoadFont("5x8.bdf")

font_large = graphics.Font()
font_large.LoadFont("7x13.bdf")

# initialize matrix
matrix = RGBMatrix(options=options)

green = graphics.Color(0, 255, 0)
red = graphics.Color(255, 0, 0)
white = graphics.Color(255, 255, 255)
grey = graphics.Color(126, 126, 126)
black = graphics.Color(0, 0, 0)
#graphics.DrawCircle(matrix, 15, 15, 10, green)
#matrix.Fill(20, 0, 0)


def displayTicker(currency='BTC', change=-30, currentPrice=35904, fiat='€'):
    graphics.DrawText(matrix, font_large, 0, 13, white, currency)
    graphics.DrawText(matrix, font_medium, 0, 26, grey,
                      str(round(currentPrice, 2))+fiat)
    if change > 0:
        graphics.DrawText(matrix, font_medium, 28, 13, green, "▲")
        graphics.DrawText(matrix, font_medium, 35, 13,
                          green, str(round(change, 2))+"%")
    elif change < 0:
        graphics.DrawText(matrix, font_medium, 28, 13, red, "▼")
        graphics.DrawText(matrix, font_medium, 35, 13,
                          red, abs(str(round(change, 2)))+"%")
    else:
        graphics.DrawText(matrix, font_medium, 28, 13, grey, "-")
        graphics.DrawText(matrix, font_medium, 35, 13, grey, '0%')
    # TODO add mini graph of 24h


def wipeScreen():
    for y in range(0, 33):
        graphics.DrawLine(matrix, 0, y-1, 63, y-1, black)
        graphics.DrawLine(matrix, 0, y, 63, y, grey)
        time.sleep(0.1)

# ask binance for a 24h rolling window ticker


def getTicker(symbol='BTCEUR'):
    return client.get_ticker(symbol=symbol)


data = getTicker()
displayTicker(change=float(
    data['priceChangePercent']), currentPrice=float(data['lastPrice']))

items = cycle(settings['24hTicker']['Pairs'])

try:
    print("Press CTRL-C to stop.")
    while True:

        current_ticker = next(items)
        ticker_data = getTicker(current_ticker)
        displayTicker(settings['24hTicker']['Pairs'][current_ticker]['ShortName'],
                      float(ticker_data['priceChangePercent']),
                      float(ticker_data['lastPrice']),
                      settings['24hTicker']['Pairs'][current_ticker]['FiatSymbol'])
        time.sleep(5)
        wipeScreen()


except KeyboardInterrupt:
    sys.exit(0)
