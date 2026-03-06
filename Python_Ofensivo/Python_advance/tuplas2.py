#!/usr/bin/env python3

mi_tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9)

numeros_impares = tuple(i for i in mi_tupla if i % 2 != 0)

print(numeros_impares)


