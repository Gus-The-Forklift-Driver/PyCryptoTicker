import time
import sys

from itertools import cycle

from matplotlib import widgets

import utils
import graphics

coinData = {}
currencies = []

settings = utils.read_config_file()

# stores all the currencies name in one variable to avoid doing too many api calls
for keys in settings['widgets']:
    currencies.append(keys['name'])
print(currencies)

currenciesNames = utils.get_names(currencies)

items = cycle(settings['widgets'])
coinData = utils.get_24h_change(currencies)
print(coinData)
try:
    print("Press CTRL-C to stop.")
    while True:

        for widget in settings['widgets']:

            if widget['type'] == 'ticker':
                pass
                # print(widget['name'])
                currentData = coinData[widget['name']]
                graphics.displayTicker(
                    currency=currenciesNames[widget['name']],
                    currentPrice=currentData['eur'],
                    change=currentData['eur_24h_change']
                )

                #currentWidget = next(items)
                # print(currentWidget)


except KeyboardInterrupt:
    sys.exit(0)
