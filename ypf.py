import pandas as pd
import yfinance as yf

#variable = [4,5,6]

#df = pd.DataFrame(variable)
#print(df)
#print(type(df))

#data_frame = yf.download("ypf")
#data_frame.to_excel("ypf.xlsx")

#READ EXCEL

#data_frame = pd.read_excel("ypf.xlsx")
#data_frame.sort_values("Date", ascending=False)
#print(data_frame)

lista_tickers = yf.download(["ypf", "ypf.ba"], start="2023-05-01")           #recordar se usan corchetes porque es una lista.-ls
lista_tickers = lista_tickers.drop (["Adj Close", "High"], axis = "columns") #recordar se usan corchetes porque es una lista.-

print(lista_tickers)