import ssl
import pandas

class Stocklists:
    @staticmethod
    def format_symbol(symbol: str) -> str:
        symbol = symbol.upper()
        if symbol.endswith('.UN'):
            symbol = symbol[:-3] + '-UN'
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