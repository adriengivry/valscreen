import os
import shutil
import yfinance as yf
import json

from .ticker import *

class Fetcher:
    def __init__(self, update: bool):
        self.appDataDir = os.path.join(os.environ['APPDATA'], 'valscreen')
        self.update = update

    def clear_cache(self):
        for filename in os.listdir(self.appDataDir):
            file_path = os.path.join(self.appDataDir, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))

    def get_ticker_filepath(self, symbol: str) -> str:
        return os.path.join(self.appDataDir, f"{symbol.upper()}.json")

    def get_cached_ticker(self, symbol: str) -> Ticker:
        # In the event an update has been requested, ignore the cache to force pulling data from Yahoo Finance
        if self.update:
            return None

        filepath = self.get_ticker_filepath(symbol)
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                jsonData = json.load(f)
                return Ticker(jsonData)
        else:
            return None

    def get_ticker_from_yahoo(self, symbol: str) -> Ticker:
        yticker = yf.Ticker(symbol)
        return Ticker(yticker.stats())

    def cache_ticker(self, ticker: Ticker):
        if not os.path.exists(self.appDataDir):
            os.makedirs(self.appDataDir)

        filepath = self.get_ticker_filepath(ticker.symbol)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(ticker.data, f, ensure_ascii=False, indent=4)

    def get_ticker(self, symbol: str, forceUpdate = False, autoCache = True):
        ticker = None if forceUpdate else self.get_cached_ticker(symbol)

        if not ticker:
            ticker = self.get_ticker_from_yahoo(symbol)

        if ticker and ticker.is_valid(): 
            if autoCache:
                self.cache_ticker(ticker)
            return ticker

        return None

    def download_tickers(self, symbols: list[str]):
        for symbol in symbols:
            self.get_ticker(symbol, True, True)
        