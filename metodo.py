def suma(a, b):
    return b - a

resultado = suma(2,3)
print(f"El resultado de la suma es {resultado}")    #STRING
print(type(resultado))                              #Class de la variable

def take_profit(precio, porcentaje):
    ejecucion_tp = precio + (1*porcentaje) # 1 * 0.05 + 105%
    return f"(RETURN) ESTE VALOR {ejecucion_tp}" #Es lo que DEVUELVE la funcion cuando es instanciada, aca sumo string con variable
print(take_profit)                                  #Object
print(type(take_profit))                            #Class de la variable

valores = take_profit(200,0.05)

print(f"Este es el RETURN de la funcion --> {valores}")                                              #Return de la función
print(f"El valor de venta por take profit es {valores}")    #Print de la variable
print(type(valores))                                        #Class de la variable
