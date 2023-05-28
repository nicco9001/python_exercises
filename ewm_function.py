import pandas as pd
import yfinance as yf


#La Media Móvil Exponencial (EMA, por sus siglas en inglés de Exponential Moving Average) es un tipo de media móvil, 
#que asigna una ponderación diferente a cada precio en un periodo de tiempo determinado. Este cálculo favorece a los 
#precios más recientes al otorgarles un peso mayor y reduciendo de manera exponencial según se retrocede en el tiempo.

ticker = yf.download("VIST")
ticker = ticker.loc [(ticker.index.year >= 2022) | (ticker.index.year == 2023) & (ticker.index.month >= 7)] # | = or
#ticker = ticker.loc [ticker.index.year >= 2022,:]
#ticker = ticker.sort_values("Date", ascending=False)
ticker = ticker.rename(columns={"Open": "Apertura", "Close": "Cierre", "Adj Close": "Adj_Close"})
ticker = ticker.drop ("Volume", axis = "columns") #también se puede usar el nro 1.-
ticker["Var %"] = ticker.Adj_Close.pct_change()*100
ticker["EMA_15"] = ticker["Adj_Close"].ewm(span = 15).mean()    #span = indica cantidad de registros para atras.-
ticker["Variacion_Nominal"] = ticker["Adj_Close"].diff()        #cierre de hoy Vs cierre de ayer.-
#ATRAS son los registros para arriba, ADELANTE son los registros para ABAJO del Data Frame.-
ticker["Variacion_FW_Nominal"] = ticker["Adj_Close"].diff(-2)   #Va para ATRAS siendo el valor de llegada el superior inmediato
                                                                #al conteo. En este caso al valor mas antigüo le resta el valor 
                                                                # mas nuevo.-

#ticker.to_excel("VISTA.xlsx", index=True)      #Para este metodo de Pandas NO se asigna variable. index se define en True para
                                                #mantener los filtros de arriba.

#print(ticker.dropna().round(2)) #round = redondeo

condicion = ticker["Apertura"] > 20.62
print(ticker[condicion].round(2))