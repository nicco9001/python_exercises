#import pandas as pd
import yfinance as yf

#list = [1, 2, 3]
#df = pd.DataFrame((list), index = ["A","B","C"])
#df.reset_index()
#print(df)

ypf = yf.download("ypf", start="2022-03-22", end="2023-03-22")
#df_ypf = df.reset_index() 
df_ypf = ypf.sort_values("Volume", ascending=False)
#df_ypf = ypf.rename (columns={"Open": "Apertura", "Close": "Cierre"})
print(df_ypf)



#variable = "Esto es una prueba"
#print(variable)