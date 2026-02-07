# 🔍 Nmap — Escáner de Puertos y Redes

> **Nmap** (Network Mapper) es una de las herramientas más utilizadas en pentesting para el descubrimiento de hosts, escaneo de puertos y fingerprinting de servicios.

📌 **Dato clave:** En total existen **65,535 puertos** (del 1 al 65535) en un sistema.

---

## 📋 Tabla Resumen de Parámetros

| Parámetro | Descripción |
|-----------|-------------|
| `-p` | Especifica el puerto o rango de puertos a escanear |
| `-p-` | Escanea **todos** los 65,535 puertos |
| `--top-ports` | Escanea los N puertos más comunes |
| `--open` | Muestra solo puertos **abiertos** |
| `-v` | Modo **verbose** (muestra información en tiempo real) |
| `-n` | **No** aplica resolución DNS (más rápido) |
| `-sV` | **Fingerprinting** — Detecta versión del servicio |
| `-sT` | Escaneo **TCP Connect** (Three-Way Handshake completo) |
| `-sn` | **Ping Sweep** — Descubre hosts activos (sin escanear puertos) |
| `-T[0-5]` | Velocidad del escaneo (0=Paranoid, 5=Insane) |

---

## 1️⃣ Escaneo por Rango de Puertos

Escanear un rango específico de puertos (ej. del 1 al 100):

```bash
nmap -p1-100 10.10.10.1
```

Escanear **todos** los puertos (1-65535):

```bash
nmap -p- 10.10.10.1
```

---

## 2️⃣ Escaneo de Top Puertos

Escanear solo los **50 puertos más comunes**:

```bash
nmap --top-ports 50 10.10.10.1
```

Escanear los top 500 puertos mostrando solo los **abiertos**:

```bash
nmap --top-ports 500 --open 10.10.10.1
```

---

## 3️⃣ Modo Verbose (`-v`)

Muestra la información del escaneo **en tiempo real** mientras se ejecuta:

```bash
nmap --top-ports 500 10.10.10.1 -v
```

---

## 4️⃣ Fingerprinting de Servicios (`-sV`)

Detecta la **versión exacta** del servicio corriendo en cada puerto. Útil para buscar vulnerabilidades conocidas:

```bash
nmap -p22,80 -sV 10.10.10.1
```

> 💡 Esto nos permite obtener información detallada como: `OpenSSH 8.2`, `Apache 2.4.41`, etc.

---

## 5️⃣ Escaneo Optimizado para Pentesting

Como atacantes nos interesa ir **lo más rápido posible**. El parámetro `-n` evita la resolución DNS (ahorra tiempo):

```bash
nmap -p- --open 10.10.10.1 -v -n
```

---

## 6️⃣ Velocidad del Escaneo — Templates (`-T`)

| Template | Nombre | Descripción |
|----------|--------|-------------|
| `-T0` | Paranoid | Extremadamente lento y **sigiloso** |
| `-T1` | Sneaky | Lento, evita detección |
| `-T2` | Polite | Reduce carga en la red |
| `-T3` | Normal | Velocidad por defecto |
| `-T4` | Aggressive | Rápido, asume red confiable |
| `-T5` | Insane | **Máxima velocidad**, puede perder paquetes |

> ⚠️ **Regla:** Cuanto más lento el escaneo → más **sigiloso** y difícil de detectar por un IDS/IPS.

```bash
nmap -p- -T5 --open 10.10.10.1 -v -n
```

---

## 7️⃣ TCP Connect Scan (`-sT`) — Three-Way Handshake

Este tipo de escaneo establece una **conexión TCP completa** (Three-Way Handshake):

```bash
nmap --top-ports 500 -T5 -sT --open 10.10.10.1 -v -n
```

### ¿Cómo funciona?

```
                PUERTO ABIERTO                    PUERTO CERRADO
               ┌──────────────┐                  ┌──────────────┐
  Atacante     │   Objetivo   │    Atacante      │   Objetivo   │
     │         │              │       │           │              │
     │── SYN ─────────►│     │       │── SYN ─────────►│       │
     │         │              │       │           │              │
     │◄── SYN/ACK ─────│     │       │◄── RST ─────────│       │
     │         │              │       │           │              │
     │── ACK ─────────►│     │       │  (Cerrado)│              │
     │  (Conexión       │     │       └──────────────┘
     │   establecida)   │     │
     └──────────────────┘
```

- **Puerto abierto:** Recibimos `SYN/ACK` → Enviamos `ACK` → Conexión **ESTABLISHED**
- **Puerto cerrado:** Recibimos `RST` → El puerto está **cerrado**

---

## 8️⃣ Captura de Tráfico con `tcpdump` + Wireshark

Para **analizar** el tráfico generado por Nmap podemos capturarlo:

### Paso 1 — Iniciar la captura en una terminal:

```bash
tcpdump -i wlan0 -w Captura.cap -v
```

> 📌 Usa `iwconfig` para verificar el nombre de tu interfaz de red.

### Paso 2 — Ejecutar Nmap en otra terminal:

```bash
nmap -p22 -sT --open 10.10.10.1 -v
```

### Paso 3 — Abrir la captura en Wireshark:

```bash
wireshark Captura.cap &>/dev/null & disown
```

> 💡 `&>/dev/null & disown` ejecuta Wireshark en segundo plano sin mostrar salida en terminal.

---

## 9️⃣ Descubrimiento de Hosts en la Red (`-sn`)

Para ver **qué dispositivos están activos** dentro de una red sin escanear puertos:

```
Red ejemplo: 10.10.10.0/24
├── Network ID:  10.10.10.0
├── Broadcast:   10.10.10.255
└── Hosts:       10.10.10.1 - 10.10.10.254
```

```bash
nmap -sn 10.10.10.0/24
```

---

## 🧰 Comando Útil Extra

Ver la tabla de rutas del sistema:

```bash
route -n
```




