import yfinance as yf
import pandas as pd

bynd = yf.download("BYND", start="2023-03-01", end="2023-03-31")
tf = pd.DataFrame(bynd)
#tf = tf.sort_index(ascending=False)
tf = tf.sort_values("Volume", ascending=False)
tf = tf.loc["2023-03-08":"2023-03-09",["Open", "Close"]] #El metodo loc se escribe de mas antigüo a mas nuevo.-
tf = tf.rename (columns={"Open": "Apertura", "Close": "Cierre"})

print(tf)
