#!/usr/bin/env python3

variable = "Soy global"

def mi_funtion():
    global variable
    variable = "Soy global y he sido modificado"
    print(variable)

mi_funtion()

print(variable)
