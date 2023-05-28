import pandas as pd
import yfinance as yf
#import colorama

#colorama.init()

ticker = yf.download("spy")
ticker = ticker.loc [(ticker.index.year == 2023) & (ticker.index.month == 3)]
ticker = ticker.rename(columns={"Open": "Apertura", "Close": "Cierre"})
ticker = ticker.drop ("Adj Close", axis = "columns") #también se puede usar el nro 1.-
ticker = ticker.sort_values("Volume", ascending=False)
ticker["Rendimiento"] = ticker.Volume.pct_change()

condicion = ticker["Volume"] >= 111746600

print(ticker.round(2))
#print(ticker[condicion]) # imprime la variable ticker con la condición aplicada.
print(condicion) #imprime de forma booleana en que valor se cumple y en cual NO la condición.
