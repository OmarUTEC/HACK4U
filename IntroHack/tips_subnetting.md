# 🧮 Subnetting — Cálculo de Subredes

> **Subnetting** es la técnica de dividir una red IP en subredes más pequeñas. Entender esto es fundamental para el reconocimiento de redes en pentesting.

---

## 📝 Conceptos Clave

| Concepto | Descripción |
|----------|-------------|
| **Network ID** | Dirección que identifica la red (primer dirección, no asignable a hosts) |
| **Broadcast** | Dirección para enviar datos a **todos** los hosts de la red (última dirección) |
| **Máscara de subred** | Define qué parte de la IP es red y qué parte es host |
| **CIDR (`/n`)** | Notación que indica cuántos bits son de red (ej: `/24` = 255.255.255.0) |
| **Operación AND** | Se aplica entre la IP y la máscara para obtener el **Network ID** |

---

## 🔧 Método de Cálculo

### Pasos:
1. Convertir la **IP** a binario
2. Convertir la **máscara** a binario
3. Aplicar operación **AND** bit a bit → Resultado = **Network ID**
4. Reemplazar los bits de host por **1s** → Resultado = **Broadcast Address**

---

## 📌 Ejemplo 1: `172.14.15.16/17`

### Datos iniciales:
- **IP:** `172.14.15.16`
- **Máscara:** `/17` → `255.255.128.0`

### Cálculo en binario:

```
  IP:       10101100.00001110.00001111.00010000   (172.14.15.16)
  Máscara:  11111111.11111111.10000000.00000000   (255.255.128.0)  /17
            ─────────────────────────────────────
  AND:      10101100.00001110.00000000.00000000   → Network ID
```

### Resultados:

| Campo | Binario | Decimal |
|-------|---------|---------|
| **Network ID** | `10101100.00001110.00000000.00000000` | `172.14.0.0` |
| **Broadcast** | `10101100.00001110.01111111.11111111` | `172.14.127.255` |
| **Rango de hosts** | — | `172.14.0.1` → `172.14.127.254` |
| **Total de hosts** | — | 2^15 - 2 = **32,766** |

---

## 📌 Ejemplo 2: `192.112.114.29/13`

### Datos iniciales:
- **IP:** `192.112.114.29`
- **Máscara:** `/13` → `255.248.0.0`

### Cálculo en binario:

```
  IP:       11000000.01110000.01110010.00011101   (192.112.114.29)
  Máscara:  11111111.11111000.00000000.00000000   (255.248.0.0)  /13
            ─────────────────────────────────────
  AND:      11000000.01110000.00000000.00000000   → Network ID
```

### Resultados:

| Campo | Binario | Decimal |
|-------|---------|---------|
| **Network ID** | `11000000.01110000.00000000.00000000` | `192.112.0.0` |
| **Broadcast** | `11000000.01110111.11111111.11111111` | `192.119.255.255` |
| **Rango de hosts** | — | `192.112.0.1` → `192.119.255.254` |
| **Total de hosts** | — | 2^19 - 2 = **524,286** |

---

## 📊 Tabla de Referencia Rápida — Máscaras Comunes

| CIDR | Máscara | Hosts disponibles | Uso típico |
|------|---------|-------------------|------------|
| `/8` | 255.0.0.0 | 16,777,214 | Redes clase A |
| `/16` | 255.255.0.0 | 65,534 | Redes clase B |
| `/24` | 255.255.255.0 | 254 | Redes clase C (LAN típica) |
| `/25` | 255.255.255.128 | 126 | Subred media |
| `/26` | 255.255.255.192 | 62 | Subred pequeña |
| `/27` | 255.255.255.224 | 30 | Subred pequeña |
| `/28` | 255.255.255.240 | 14 | Segmento mínimo |
| `/30` | 255.255.255.252 | 2 | Enlace punto a punto |
| `/32` | 255.255.255.255 | 1 | Host individual |

---

## 💡 Tips Rápidos

- **Fórmula de hosts:** `2^(32-CIDR) - 2` (se restan Network ID y Broadcast)
- La operación **AND** entre IP y máscara **siempre** da el Network ID
- Para obtener el **Broadcast**: toma el Network ID y pon todos los bits de host en `1`
- En pentesting, conocer el rango de la red te permite hacer **host discovery** con `nmap -sn`
