# '()' defines a tuple which is immutable
stock_watchlist = ("GOOG", "MSFT", "AAPL")

print("watching:")
for stock in stock_watchlist:
    print(stock)

# new values get set to the tuple
stock_watchlist = ("GOOG", "MSFT", "AMZN", "AAPL", "TSLA", "TWTR")

print("\nwatching (updated):")
for stock in stock_watchlist:
	print(stock)

# notes
    # use a tuple when you have values you do not want to change
    # '("GOOG")' the use of a trailing comma defines a tuple with one item