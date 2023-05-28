variable = input("Debes ingresar la palabra HOLA: ")

while variable != "HOLA":
    print("Debes ingresar un HOLA")
    variable = input()
    if variable == "HOLA":
        print("Pasamos a la siguiente sentencia")
    else:
        print("LOCURA")
#else:
    print("TODO OK")

