#!/usr/bin/env python3

mi_conjunto = {1, 2, 3}
mi_conjunto.update({4,5,6})

mi_conjunto.remove(2)

print(mi_conjunto)

mi_conjunto.discard(5)

print(mi_conjunto)


