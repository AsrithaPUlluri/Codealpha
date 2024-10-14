#Task 2:Stock Portfolio tracker
import requests # type: ignore
import json

# Alpha Vantage API key
API_KEY = '58YW04IBZUGXNLBS'

#Stock symbols: AAPL,GOOGL,MSFT,TSLA,AMZN

# Base URL for Alpha Vantage API
BASE_URL = 'https://www.alphavantage.co/query'

# Function to get stock data from Alpha Vantage
def get_stock_data(symbol):
    params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': symbol,
        'apikey': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    if 'Time Series (Daily)' in data:
        return data['Time Series (Daily)']
    else:
        print("Error fetching data. Please check the stock symbol or API key.")
        return None

# Function to display stock information
def display_stock_info(stock_data, symbol):
    if stock_data:
        print(f"\nStock information for {symbol}:")
        latest_date = list(stock_data.keys())[0]
        latest_data = stock_data[latest_date]
        print(f"Date: {latest_date}")
        print(f"Open: {latest_data['1. open']}")
        print(f"High: {latest_data['2. high']}")
        print(f"Low: {latest_data['3. low']}")
        print(f"Close: {latest_data['4. close']}")
        print(f"Volume: {latest_data['5. volume']}")
    else:
        print("No data available.")

# Portfolio management class
class Portfolio:
    def _init_(self):
        self.stocks = {}

    def add_stock(self, symbol, quantity):
        if symbol in self.stocks:
            self.stocks[symbol] += quantity
        else:
            self.stocks[symbol] = quantity

    def remove_stock(self, symbol, quantity):
        if symbol in self.stocks:
            if self.stocks[symbol] > quantity:
                self.stocks[symbol] -= quantity
            elif self.stocks[symbol] == quantity:
                del self.stocks[symbol]
            else:
                print("Error: Not enough quantity to remove.")
        else:
            print("Error: Stock not found in portfolio.")

    def track_performance(self):
        for symbol, quantity in self.stocks.items():
            print(f"\nTracking {symbol}:")
            stock_data = get_stock_data(symbol)
            display_stock_info(stock_data, symbol)

def main():
    portfolio = Portfolio()
    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add stock")
        print("2. Remove stock")
        print("3. Track performance")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            symbol = input("Enter stock symbol: ").upper()
            quantity = int(input("Enter quantity: "))
            portfolio.add_stock(symbol, quantity)
            print(f"Added {quantity} of {symbol} to portfolio.")
        elif choice == '2':
            symbol = input("Enter stock symbol: ").upper()
            quantity = int(input("Enter quantity: "))
            portfolio.remove_stock(symbol, quantity)
            print(f"Removed {quantity} of {symbol} from portfolio.")
        elif choice == '3':
            portfolio.track_performance()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select again.")

if _name_ == "_main_":
    main()

