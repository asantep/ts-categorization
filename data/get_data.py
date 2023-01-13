"""
This file loads stock data from yahoo finance using the yfinance package
"""

import yfinance as yf
import itertools
import constants


def main(market_data=constants.STOCKS):
    match market_data:
        case constants.STOCKS:
            get_stock_data


    if market_data == "S":
        get_stock_data()
    get_bond_data()
    get_currency_data()


def get_stock_data():
    print("it works")


def get_bond_data():
    print("bonds")


def get_currency_data():
    print("currency")


if __name__ == "__main__":
    main()