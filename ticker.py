import time
import sys

from itertools import cycle


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

#items = cycle(settings['widgets'])

try:
    print("Press CTRL-C to stop.")
    while True:
        coinData = utils.get_24h_change(currencies)
        for widget in settings['widgets']:
            if widget['type'] == 'ticker':
                pass
                # print(widget['name'])
                currentData = coinData[widget['name']]
                graphics.displayTicker(
                    currency=currenciesNames[widget['name']],
                    currentPrice=currentData[str(widget['vs_currency'])],
                    change=currentData[str(
                        widget['vs_currency']+'_24h_change')]
                )
            time.sleep(10)
            graphics.wipeScreen()
    #currentWidget = next(items)
    # print(currentWidget)


except KeyboardInterrupt:
    sys.exit(0)
