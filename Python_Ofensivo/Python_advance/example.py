#!/usr/bin/env python3

ip_address = "193.168.1.39"

my_ports = [22, 21, 443]

my_ports += [80, 87, 34]

my_ports = sorted(my_ports)

del my_ports[2]

for port in my_ports:
    print(f"Puerto: {port}")
