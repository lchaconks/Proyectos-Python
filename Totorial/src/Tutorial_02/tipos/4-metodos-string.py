

#Funciones o métodos para los String

animal = "  chanCHito feliz   "
print(animal.upper()) #El método "upper" coloca todas las letras en mayúsculas
print(animal.lower()) #El método "lower" coloca todas las letras en minúsculas
print(animal.strip().capitalize()) #El método "capitalize" coloca la primera letra en mayúscula
print(animal.title())  # El método "title" coloca las primeras letras en mayúscula
print(animal.strip())  #El método "strip" elimina los espacios en blanco del lado derecho e izquierdo
print(animal.lstrip())  #El método "lstrip" elimina los espacios en blanco del lado derecho
print(animal.rstrip())  #El método "rstrip" elimina los espacios en blanco del lado izquierdo
print(animal.find("CH")) #EL método "find" contara la posición del marcador del string que indiquemos
print(animal.replace("nCH", "j")) #El método "replace" reemplaza los caracteres que le indiquemos en los parámetros
print("nCH" in animal)

#Podemos encadenar métodos para dar un formato deseado