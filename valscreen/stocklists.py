from cmath import nan
import ssl
import pandas
import html5lib

class Stocklists:
    @staticmethod
    def format_symbol(symbol: str) -> str:
        symbol = symbol.upper()
        if symbol.endswith('.UN'):
            symbol = symbol[:-3] + '-UN'
        elif symbol.endswith('.A'):
            symbol = symbol[:-2] + '-A'
        elif symbol.endswith('.B'):
            symbol = symbol[:-2] + '-B'
        elif symbol.endswith('.C'):
            symbol = symbol[:-2] + '-C'
        return symbol

    @staticmethod
    def set_ssl_certificate():
        ssl._create_default_https_context = ssl._create_unverified_context

    def _format_list(elements: list[str]) -> list:
        return [Stocklists.format_symbol(element) for element in elements]

    @staticmethod
    def get_sp500_list() -> list:
        Stocklists.set_ssl_certificate()
        return Stocklists._format_list(pandas.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies', header=0)[0]['Symbol'].tolist())

    @staticmethod
    def get_dow_list() -> list:
        Stocklists.set_ssl_certificate()
        return Stocklists._format_list(pandas.read_html('https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average', header=0)[1]['Symbol'].tolist())

    @staticmethod
    def get_tsx60() -> list:
        Stocklists.set_ssl_certificate()
        symbols = pandas.read_html('https://en.wikipedia.org/wiki/S%26P%2FTSX_60', header=0)[0]['Symbol'].tolist()
        # For some reason, one of the ticker on the S&P/TSX60 list on Wikipedia is NaN, so we ignore it
        symbols = [x for x in symbols if str(x) != 'nan']
        symbols = Stocklists._format_list(symbols)
        return [symbol + '.TO' for symbol in symbols]