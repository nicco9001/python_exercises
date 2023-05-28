preguntas = {
    "Cómo se llama la mascota? ": None,
    "Edad ": None,
    "Cómo se llama el dueño ": None
}

for respuesta in preguntas.keys(): #usamos el metodo keys para asignar el value correspondiente
    preguntas [respuesta] = input(respuesta) 

#respuesta es el item a iterar, se reemplaza el None por los datos ingresados con el input.-

print(preguntas)
