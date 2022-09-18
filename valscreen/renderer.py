from ctypes import alignment
import math
import numbers
import re
from types import NoneType
from unittest import result
import prettytable
from datetime import date, datetime
import plotext as plt
import colorama
from colorama import Fore, Back, Style
import csv

from .analysis import *

class Renderer:
    def __init__(self):
        colorama.init()

    def drawScreeningTable(self, results: list[TickerAnalysis]):
        # Prepare
        self.table = prettytable.PrettyTable(self.get_formatted_headers(results))
        self.table.title = "Security Value Screening"
        self.table.set_style(prettytable.DOUBLE_BORDER)

        # Fill
        for result in results:
            formattedValues = list()
            for key, value in result.entries.items():
                str = None
                if isinstance(value, numbers.Number):
                    if value == nan:
                        str = self.format_nan(value)
                    elif 'Ratio' in key:
                        str = self.format_percentage(value)
                        color = None
                        if value > 1: color = Fore.GREEN
                        elif value > 0.75: color = Fore.YELLOW
                        else: color = Fore.RED
                        str = f"{color}{str}{Style.RESET_ALL}"

                    else:
                        str = self.format_number(value)
                else:
                    str = value
                formattedValues.append(str)

            self.table.add_row(formattedValues)

        # Print
        print(self.table)
        self.table = None

    def get_formatted_headers(self, results: list[TickerAnalysis]) -> list:
        headers = list()

        if len(results) > 0:
            headers += results[0].entries.keys()
        
        return headers

    def format_number(self, n):
        return f'{round(n, 2):,}'

    def format_percentage(self, n):
        return f'{round(n * 100.0, 2):,}%'

    def format_nan(self):
        return Fore.BLACK + Style.BRIGHT + 'N/A'+ Style.RESET_ALL