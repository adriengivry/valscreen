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

        grahamNumber = math.sqrt(22.5 * ticker.trailingEps * ticker.bookValue)
        serenityNumber = math.sqrt(12 * ticker.trailingEps * ticker.bookValue)
        defensiveIntrinsicValue = grahamNumber / ticker.price
        entreprisingIntrinsicValue = serenityNumber / ticker.price

        self.entries['Symbol'] = ticker.symbol
        self.entries['Company Name'] = ticker.companyName
        self.entries['Sector'] = ticker.sector
        self.entries['Industry'] = ticker.industry
        self.entries['Price'] = ticker.price
        self.entries['Graham Number'] = grahamNumber
        self.entries['Serenity Number'] = serenityNumber
        self.entries['Defensive Ratio'] = defensiveIntrinsicValue
        self.entries['Entreprising Ratio'] = entreprisingIntrinsicValue

        return True
        