#!/usr/bin/env python3

db1_credential = ("s4vitar", "s4vitar123")
db2_credential = ("hackermate", "hackermate123")

try :
    db1_credential[0] = "Sharuko"
except TypeError:
    print("No es posible manipular los elementos de una tupla")


