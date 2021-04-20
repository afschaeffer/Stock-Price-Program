# Amy Schaeffer Assignment 7.1
# Program that uses key-value pairs ot display stock prices on companies in the dictionary.

ent_stock = {
    "DIS": 106.06,
    "AMC": 3.36,
    "UVV": 46.06,
    "NFLX": 421.38,
    "FB": 187.50,
    "GOOGL": 1270.86,
    "CMCSA": 38.21,
    "FOX": 26.01,
    "CBS": 0.065,
    "MSFT": 174.05
}
while True:
    entry = input("Please enter a ticker symbol: ")
    entry_upper = entry.upper()
    if entry_upper in ent_stock:
        print(f"Ticker sybmol: {entry_upper}")
        print(f"Stock Price 4/27/20: {ent_stock[entry_upper]} USD")
    if entry_upper not in ent_stock:
        print("Ticker symbol invalid")
    stay = input('Type "q" to quit, or enter any key to return to prompt: ')
    if stay == "q":
        break


