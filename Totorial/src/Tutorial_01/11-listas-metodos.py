lenguajes = ["Python", "Ruby", "PHP", "Javascript", "Java"]
lenguajes.insert(3, "Go") #Insertar datos en la posicion 3
lenguajes.insert(0, "C")  #Insertar datos en la posición 0
lenguajes.remove("Ruby")  #Remover un dato especifico
print("PHP" in lenguajes)  #(in) para buscar un dato dentro de la variable
# lenguajes.clear()

print(len(lenguajes))