# ValScreen
ValScreen is a command-line quantitative stock screener for publicly-traded companies in the United States and Canada. 

## Installation
```properties
pip install -r requirements.txt
pip install -e .
```

## Examples
```properties
# Show Help Message
valscreen --help

# Run the quantitative stock screener over a list of 4 symbols
valscreen AAPL,INTC,TXN,LOGI

# Run the quantitative stock screener over the S&P500 index
valscreen ~sp500

# Run the quantitative stock screener over the S&P500 index and BMO.TO
valscreen ~sp500,BMO.TO

# Run the quantitative stock screener over the Dow Jones Industrial Average (DJIA) index, while forcing tickers to update (ignore cached data, slower but ensures the data is up-to-date)
valscreen ~dow
```

## Example of screening with the Dow Jones Industrial Average
```
╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                  Security Value Screening                                                                                 ║
╠════════╦═════════════════════════════════╦════════════════════════╦═════════════════════════════════════╦════════╦═══════════════╦═════════════════╦═════════════════╦════════════════════╣
║ Symbol ║           Company Name          ║         Sector         ║               Industry              ║ Price  ║ Graham Number ║ Serenity Number ║ Defensive Ratio ║ Entreprising Ratio ║
╠════════╬═════════════════════════════════╬════════════════════════╬═════════════════════════════════════╬════════╬═══════════════╬═════════════════╬═════════════════╬════════════════════╣
║  WBA   ║  Walgreens Boots Alliance, Inc. ║       Healthcare       ║       Pharmaceutical Retailers      ║ 34.27  ║      63.5     ║      46.37      ║      185.3%     ║      135.32%       ║
║   GS   ║ Goldman Sachs Group, Inc. (The) ║   Financial Services   ║           Capital Markets           ║ 326.21 ║     572.27    ║      417.93     ║     175.43%     ║      128.12%       ║
║  INTC  ║        Intel Corporation        ║       Technology       ║            Semiconductors           ║ 29.24  ║     50.84     ║      37.13      ║     173.87%     ║      126.98%       ║
║  DOW   ║             Dow Inc.            ║    Basic Materials     ║              Chemicals              ║ 46.42  ║     72.82     ║      53.18      ║     156.87%     ║      114.56%       ║
║  JPM   ║      JP Morgan Chase & Co.      ║   Financial Services   ║          Banks—Diversified          ║ 117.08 ║     155.68    ║      113.69     ║     132.97%     ║       97.1%        ║
║   VZ   ║   Verizon Communications Inc.   ║ Communication Services ║           Telecom Services          ║ 41.25  ║     47.91     ║      34.98      ║     116.13%     ║       84.81%       ║
║  TRV   ║  The Travelers Companies, Inc.  ║   Financial Services   ║    Insurance—Property & Casualty    ║ 162.33 ║     176.66    ║      129.02     ║     108.83%     ║       79.48%       ║
║  CVX   ║       Chevron Corporation       ║         Energy         ║         Oil & Gas Integrated        ║ 156.45 ║     162.66    ║      118.79     ║     103.97%     ║       75.93%       ║
║  CSCO  ║       Cisco Systems, Inc.       ║       Technology       ║       Communication Equipment       ║  43.3  ║     24.78     ║       18.1      ║      57.23%     ║       41.79%       ║
║  MRK   ║      Merck & Company, Inc.      ║       Healthcare       ║      Drug Manufacturers—General     ║ 87.72  ║     50.16     ║      36.63      ║      57.18%     ║       41.76%       ║
║  AXP   ║     American Express Company    ║   Financial Services   ║           Credit Services           ║ 153.08 ║     82.51     ║      60.26      ║      53.9%      ║       39.36%       ║
║  MMM   ║            3M Company           ║      Industrials       ║            Conglomerates            ║ 116.61 ║     62.34     ║      45.53      ║      53.46%     ║       39.04%       ║
║  CAT   ║        Caterpillar, Inc.        ║      Industrials       ║ Farm & Heavy Construction Machinery ║ 179.47 ║      91.5     ║      66.82      ║      50.98%     ║       37.23%       ║
║  IBM   ║ International Business Machines ║       Technology       ║   Information Technology Services   ║ 127.27 ║     54.26     ║      39.63      ║      42.63%     ║       31.14%       ║
║  WMT   ║           Walmart Inc.          ║   Consumer Defensive   ║           Discount Stores           ║ 133.19 ║     56.62     ║      41.35      ║      42.51%     ║       31.05%       ║
║  DIS   ║    Walt Disney Company (The)    ║ Communication Services ║            Entertainment            ║ 108.25 ║     44.29     ║      32.34      ║      40.91%     ║       29.88%       ║
║  JNJ   ║        Johnson & Johnson        ║       Healthcare       ║      Drug Manufacturers—General     ║ 167.6  ║      67.0     ║      48.93      ║      39.98%     ║       29.2%        ║
║  HON   ║   Honeywell International Inc.  ║      Industrials       ║            Conglomerates            ║ 177.35 ║     65.53     ║      47.86      ║      36.95%     ║       26.98%       ║
║   PG   ║  Procter & Gamble Company (The) ║   Consumer Defensive   ║    Household & Personal Products    ║ 138.28 ║     49.98     ║       36.5      ║      36.15%     ║       26.4%        ║
║  UNH   ║ UnitedHealth Group Incorporated ║       Healthcare       ║           Healthcare Plans          ║ 521.02 ║     183.14    ║      133.75     ║      35.15%     ║       25.67%       ║
║  MSFT  ║      Microsoft Corporation      ║       Technology       ║       Software—Infrastructure       ║ 244.74 ║      69.6     ║      50.83      ║      28.44%     ║       20.77%       ║
║  NKE   ║            Nike, Inc.           ║   Consumer Cyclical    ║        Footwear & Accessories       ║ 104.12 ║     28.65     ║      20.92      ║      27.51%     ║       20.09%       ║
║   KO   ║     Coca-Cola Company (The)     ║   Consumer Defensive   ║       Beverages—Non-Alcoholic       ║ 59.54  ║     16.22     ║      11.85      ║      27.25%     ║       19.9%        ║
║   V    ║            Visa Inc.            ║   Financial Services   ║           Credit Services           ║ 193.3  ║     49.07     ║      35.84      ║      25.39%     ║       18.54%       ║
║  CRM   ║         Salesforce, Inc.        ║       Technology       ║         Software—Application        ║ 151.51 ║     26.27     ║      19.19      ║      17.34%     ║       12.66%       ║
║  AMGN  ║            Amgen Inc.           ║       Healthcare       ║      Drug Manufacturers—General     ║ 231.14 ║     34.59     ║      25.26      ║      14.97%     ║       10.93%       ║
║  AAPL  ║            Apple Inc.           ║       Technology       ║         Consumer Electronics        ║ 150.7  ║     22.17     ║      16.19      ║      14.71%     ║       10.74%       ║
║   HD   ║      Home Depot, Inc. (The)     ║   Consumer Cyclical    ║       Home Improvement Retail       ║ 275.97 ║      9.2      ║       6.72      ║      3.33%      ║       2.43%        ║
╚════════╩═════════════════════════════════╩════════════════════════╩═════════════════════════════════════╩════════╩═══════════════╩═════════════════╩═════════════════╩════════════════════╝
```

## Usage
```
usage: valscreen [-h] [-u] [-c] stocklist

positional arguments:
  stocklist     list of companies symbols (or presets: ~sp500, ~dow) to screen through (ex: aapl,~dow,txn)

options:
  -h, --help    show this help message and exit
  -u, --update  force updating tickers by pulling data from yahoo finance even for previously cached tickers (can be very slow when dealing with a lot of tickers)
  -c, --clear   clears the cache before the analysis (NOT RECOMMENDED, VERY SLOW)
```

## Limitations
This software is currently limited to company listed on Canadian and American stock exchanges.

## Formula References and Disclaimers
The formula used in this program are adaptations of Graham's formula for:
- *Graham Number*
- *Serenity Number*

Reference: https://www.grahamvalue.com/quick-reference

**Notes:**
- *Graham Number* original formula uses the average EPS of the past three years, while this software uses trailing EPS (1 year).
- *Serenity Number* original formula uses the Tangible Book Value Per Share (TBVPS), while this softare uses the Book Value Per Share (BVPS)

## Roadmap
- Updating *Graham Number* calculation to use the average EPS of the past three years
- Updating *Senerity Number* calculation to use the Tangible Book Value Per Share (TBVPS)