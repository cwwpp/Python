import requests
import tkinter as tk
from datetime import datetime

def trackBitcoin():
    url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR"
    response = requests.get(url).json()
    USDPrice = response["USD"]
    EURPrice = response["EUR"]
    JPPrice = response["JPY"]
    time = datetime.now().strftime("%H:%M:%S %d/%m/%y")

    labelUSDPrice.config(text = "$" + str(USDPrice))
    labelEURPrice.config(text = "€" + str(EURPrice))
    labelJPPrice.config(text = "¥" + str(JPPrice))
    labelTime.config(text = "TIME: " + time)

    window.after(1000, trackBitcoin)

window = tk.Tk()
window.geometry("300x350")
window.title("Bitcoin Tracker")

f1 = ("poppins", 24, "bold")
f2 = ("poppins", 22, "bold")
f3 = ("poppins", 18, "normal")

label = tk.Label(window, text = "BITCOIN PRICE", font = f1)
label.pack(pady = 20)

labelUSDPrice = tk.Label(window, font = f2)
labelUSDPrice.pack(pady = 0)

labelEURPrice = tk.Label(window, font = f2)
labelEURPrice.pack(pady=0)

labelJPPrice = tk.Label(window, font = f2)
labelJPPrice.pack(pady = 0)

labelTime = tk.Label(window, font = f3)
labelTime.pack(pady = 10)

trackBitcoin()

window.mainloop()
