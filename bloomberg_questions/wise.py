#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'printBalances' function below.
# If required, please use getMidMarketRate(fromCcy, toCcy) function to get the mid market rates for a currency pair
# The function is expected to return a STRING containing balances in the multi currency account in alphabetical order of balance currencies.
# The function accepts STRING_ARRAY requestes as parameter. Each String is in the format <Request Action>,<Request Amount>,<Request Currency>
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY requests as parameter.
#


def printBalances(requests):
    # Currencies in priority order
    currencies = ["USD", "EUR", "GBP"]
    balances = {"USD": 0.00, "EUR": 0.00, "GBP": 0.00}

    # Round to 2 decimal places, using math.ceil to round up
    def roundUp(val):
        result = str(math.ceil(100 * val) / 100)
        # If only 1 dp
        if len(result.split(".")[1]) < 2:
            result += "0"
        return result

    def handleRequest(request):
        (action, amount, currency) = request.split(",")
        amount = float(amount)

        # If depositing, deposit amount then continue to next request
        if action == "DEPOSIT":
            balances[currency] += amount
            return

        # If sufficient balance in correct currency, remove from that wallet, then continue to next request
        if balances[currency] >= amount:
            balances[currency] -= amount
            return

        amount -= balances[currency]

        # Else if sufficient balance in one other currency (USD -> EUR -> GBP)
        for otherCurrency in currencies:
            if otherCurrency == currency:
                continue

            convertedAmount = amount / getMidMarketRate(otherCurrency, currency)
            if convertedAmount < balances[otherCurrency]:
                balances[otherCurrency] -= convertedAmount
                balances[currency] = 0
                amount = 0
                return

        # Else if sufficient balance in multiple other currencies (USD -> EUR -> GBP)
        for otherCurrency in currencies:
            if otherCurrency == currency:
                continue

            convertedAmount = amount / getMidMarketRate(otherCurrency, currency)
            # If more than in current wallet
            if convertedAmount < balances[otherCurrency]:
                balances[otherCurrency] -= convertedAmount
                balances[currency] = 0
                break

        # Else
        #     Deny

        # Only return non-zero balances
        # Return in alphabetical order of currency
        # Round to 2dp, always round up

    for request in requests:
        handleRequest(request)

    result = []
    if balances["EUR"] > 0:
        result.append(roundUp(balances["EUR"]) + " EUR")
    if balances["GBP"] > 0:
        result.append(roundUp(balances["GBP"]) + " GBP")
    if balances["USD"] > 0:
        result.append(roundUp(balances["USD"]) + " USD")

    return ", ".join(result)


rates = {
    "GBP-USD": 1.30,
    "USD-GBP": 0.7692,
    "GBP-EUR": 1.20,
    "EUR-GBP": 0.8333,
    "EUR-USD": 1.10,
    "USD-EUR": 0.9090,
}

# This function can be used in your solution to get the daily mid market rate for a currency pair
def getMidMarketRate(fromCurrency, toCurrency):
    if fromCurrency == toCurrency:
        return 1.0

    if fromCurrency + "-" + toCurrency in rates.keys():
        return rates[fromCurrency + "-" + toCurrency]
    else:
        raise Exception(
            "unable to find rate between "
            + fromCurrency.upper()
            + " and "
            + toCurrency.upper()
        )


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    requests_count = int(input().strip())

    requests = []

    for _ in range(requests_count):
        requests_item = input()
        requests.append(requests_item)

    result = printBalances(requests)

    fptr.write(result + "\n")

    fptr.close()
