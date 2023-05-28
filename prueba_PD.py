import pandas as pd

lista = [1,2,3]

data_frame = pd.DataFrame(lista)
#data_frame.columns = ["Index"] #siendo solo un dato USAR CORCHETES.-
data_frame ["columna_B"] = 2      
data_frame.columns = ("Index", "Row") # También se puede usar CORCHETES.-
data_frame.index = ("A", "B", "C")
data_frame.sort_index(ascending=False)
print(data_frame)

#print(f"La version de Pandas es {pd.__version__}")

#Para chequear version en Terminal usar pip show y nombre de LIBRERIA ej pip show pandas.
#Se pueden listar todos los paquetes instalados mediante pip list

