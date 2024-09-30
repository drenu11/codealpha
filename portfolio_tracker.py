import yfinance as yf

portfolio = {}

def add_stock(ticker, shares):
    portfolio[ticker] = shares

def remove_stock(ticker):
    if ticker in portfolio:
        del portfolio[ticker]

def track_portfolio():
    total_value = 0
    for ticker, shares in portfolio.items():
        stock = yf.Ticker(ticker)
        price = stock.history(period='1d')['Close'][0]
        total_value += price * shares
        print(f"{ticker}: {shares} shares at ${price:.2f} each -> Total: ${price * shares:.2f}")
    print(f"Total Portfolio Value: ${total_value:.2f}")

def main():
    while True:
        print("\nOptions:")
        print("1. Add stock")
        print("2. Remove stock")
        print("3. Track portfolio")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            ticker = input("Enter the stock ticker symbol (e.g., AAPL): ")
            shares = int(input("Enter the number of shares: "))
            add_stock(ticker, shares)
        elif choice == '2':
            ticker = input("Enter the stock ticker symbol to remove: ")
            remove_stock(ticker)
        elif choice == '3':
            track_portfolio()
        elif choice == '4':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
