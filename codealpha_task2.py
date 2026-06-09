 # Stock Portfolio Tracker

# Hardcoded stock prices
stock_price = {
              "AAPL": 180,
              "TSLA": 250,
              "GOOGL": 140,
              "MSFT": 420,
              "AMZN": 190
}

total_investment = 0

print("avaliable stock:")
for stock , price in stock_price.items():
    print(f"{stock} : ${price}")

n = int (input("enter the no of stock you own :"))
         
for i in range(n):
   stock_name = input("enter stock name :").upper()
    
   if stock_name in stock_price:
   
    quantity = int(input("enter quantity :"))
    investment = stock_price[stock_name]*quantity
    total_investment += investment
    
    print(f"Investment in {stock_name}: ${investment}")
   
   else:
    print("stock not found")

print("\ntotal investment value : $" , investment)

with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment Value: ${total_investment}")

print("Portfolio details saved to portfolio.txt")