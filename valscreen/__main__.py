import sys
import argparse

from valscreen.stocklists import Stocklists

from .renderer import *
from .analysis import *
from .fetcher import *

def get_key(tickerAnalysis: TickerAnalysis):
    return tickerAnalysis.entries['Defensive Ratio']

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(dest='stocklist', help='list of companies (or preset lists: ~sp500, ~dow) to screen through (ex: aapl,~dow,txn)')
    parser.add_argument('-u', '--update', action='store_true', dest='update', help='force updating tickers by pulling data from yahoo finance even for previously cached tickers (can be very slow when dealing with a lot of tickers)')
    parser.add_argument('-c', '--clear', action='store_true', dest='clear', help='clears the cache before the analysis (NOT RECOMMENDED, VERY SLOW)')
    args = parser.parse_args()

    symbols = list()

    stocklistElements = args.stocklist.split(',')
    for element in stocklistElements:
        if element.startswith('~'):
            preset = element[1:]
            if preset == 'sp500':
                symbols += Stocklists.get_sp500_list()
            elif preset == 'dow':
                symbols += Stocklists.get_dow_list()
        else:
            symbols.append(element.upper())

    symbols = set(symbols)

    fetcher = Fetcher(args.update)
    renderer = Renderer()

    if args.clear:
        fetcher.clear_cache()

    results = list[TickerAnalysis]()

    for symbol in symbols:
        ticker = fetcher.get_ticker(symbol)
        if not ticker.has_incomplete_data():
            tickerAnalysis = TickerAnalysis(ticker)
            # Add the ticker analysis result to the result list is the analysis was successful
            if tickerAnalysis.run_analysis():
                results.append(tickerAnalysis)

    results.sort(key=get_key, reverse=True)

    renderer.drawScreeningTable(results)

    return 0

if __name__ == '__main__':
    sys.exit(main())