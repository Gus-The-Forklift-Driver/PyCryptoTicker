import yaml
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()


def read_config_file(file='config.yml'):
    try:
        with open(file, "r") as ymlfile:
            cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
    except:
        raise TypeError('ConfigReadFail')
    else:
        return cfg


def get_price(currency='bitcoin', vs_currency='EUR'):
    return cg.get_price(currency, vs_currency)


def get_24h_change(currency='bitcoin', vs_currency='EUR'):
    return cg.get_price(currency, vs_currency, include_24hr_change=True)


def get_names(currency='bitcoin'):
    out = {}
    coinList = cg.get_coins_list()
    for key in coinList:

        if key['id'] in currency:
            out[key['id']] = key['symbol']
    return out
