from cmath import nan
import math

from .ticker import *

class TickerAnalysis:
    def __init__(self, ticker: Ticker):
        self.ticker = ticker
        self.entries = dict[str, object]()

    def run_analysis(self) -> bool:
        # Make sure we do not try to run the analysis on tickers with incomplete data
        assert(not self.ticker.has_incomplete_data())

        ticker = self.ticker

        # Analysis Failed: Cannot compute Graham and Serenity Numbers
        if ticker.trailingEps <= 0 or ticker.bookValue <= 0:
            return False

        # Analysis Failed: Market price too low
        if ticker.price <= 0.01:
            return False

        defensivePrice = math.sqrt(22.5 * ticker.trailingEps * ticker.bookValue)
        entreprisingPrice = math.sqrt(12 * ticker.trailingEps * ticker.bookValue)
        defensiveRatio = defensivePrice / ticker.price
        entreprisingRatio = entreprisingPrice / ticker.price

        self.entries['Symbol'] = ticker.symbol
        self.entries['Company Name'] = ticker.companyName
        self.entries['Sector'] = ticker.sector
        self.entries['Industry'] = ticker.industry
        self.entries['Price'] = ticker.price
        self.entries['Defensive Price'] = defensivePrice
        self.entries['Entreprising Price'] = entreprisingPrice
        self.entries['Defensive Ratio'] = defensiveRatio
        self.entries['Entreprising Ratio'] = entreprisingRatio

        return True
        