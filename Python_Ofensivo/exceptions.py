#!/usr/bin/env python3 

try:
    num = 'Hola'/0

except ZeroDivisionError:
    print("No se puede dividir un numero entre 0")

except TypeError:
    print("La operaciones matematicas solo deben realizarse con numeros")

else:
    print(f"La division de ambos numeros da como reaultado {num}")

finally:
    print("Esto siempre se va a ejecutar")



