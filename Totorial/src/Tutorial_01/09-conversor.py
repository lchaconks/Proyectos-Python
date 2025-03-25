

temperatura = float(input("Ingresa temperatura:"))
escala = input("Escribe (F) para Farengeing o (C) para Celcius:").lower()

#print(temperatura,escala)

if escala == "f":
    celsius = (temperatura - 32) * 5/9
    print(celsius)
elif escala == "c":
    fahrenheit = temperatura * 1.8 +32
    print(fahrenheit)
else:
    print("Escala incorrecta")

