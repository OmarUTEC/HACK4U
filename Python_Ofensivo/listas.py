#!/usr/bin/env python3 

puertos_tcp = [21, 22, 25, 80, 443, 8080, 445, 69]

#print(puertos_tcp)

# for puerto in puertos_tcp:
#    print(f"Este es el puerto {puerto}")


cve_list = ['CVE-2023-1435', 'CVE-2022-45761', 'CVE-2023-7863']

puertos_tcp.append(1666)

#print(puertos_tcp)

attacks = ['Phishing', 'DDoS', 'SQL Injection', 'Man In The Middle', 'Cross-Site Scripting']

print(attacks)

attacks.reverse()

print(attacks)


i = 0
while i < len(attacks):
    print(attacks[i])
    i +=1



