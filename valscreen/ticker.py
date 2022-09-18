from cmath import nan

class Ticker:
    def __init__(self, data: dict):
        # Store data
        self.data = data

        # Prepare data
        self.symbol = self.data.get('symbol', None)

        summaryProfile = self.data.get('summaryProfile', None)
        defaultKeyStatistics = self.data.get('defaultKeyStatistics', None)
        price = self.data.get('price', None)

        self.companyName = price and price.get('shortName', None) or None
        self.sector = summaryProfile and summaryProfile.get('sector', None) or None
        self.industry = summaryProfile and summaryProfile.get('industry', None) or None
        self.trailingEps = defaultKeyStatistics and defaultKeyStatistics.get('trailingEps', None) or None
        self.bookValue = defaultKeyStatistics and defaultKeyStatistics.get('bookValue', None) or None
        self.shares = defaultKeyStatistics and defaultKeyStatistics.get('sharesOutstanding', None) or None
        self.price = price and price.get('regularMarketPrice', None) or None

    def has_incomplete_data(self):
        return not self.symbol\
            or not self.companyName\
            or not self.sector\
            or not self.industry\
            or not self.price\
            or not self.trailingEps\
            or not self.bookValue\
            or not self.shares

    def is_valid(self):
        return self.data != None
    