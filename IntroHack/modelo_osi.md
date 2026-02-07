# 🌐 Modelo OSI — Las 7 Capas de Red

> El **Modelo OSI** (Open Systems Interconnection) es un modelo de referencia que divide la comunicación en redes en **7 capas**. Cada capa tiene una función específica y se comunica con las capas adyacentes.

---

## 📊 Tabla de las 7 Capas

| # | Capa | Función Principal | Protocolos / Ejemplos | PDU (Unidad de datos) |
|---|------|-------------------|-----------------------|-----------------------|
| **7** | 🖥️ **Aplicación** | Interfaz directa con el usuario y las aplicaciones | HTTP, HTTPS, FTP, SSH, DNS, SMTP | Datos |
| **6** | 🔤 **Presentación** | Traduce, cifra y comprime los datos | SSL/TLS, JPEG, ASCII, GIF | Datos |
| **5** | 🔗 **Sesión** | Establece, mantiene y cierra sesiones entre aplicaciones | NetBIOS, RPC, SMB | Datos |
| **4** | 🚛 **Transporte** | Entrega fiable (TCP) o rápida (UDP) de extremo a extremo | **TCP**, **UDP** | Segmento / Datagrama |
| **3** | 🗺️ **Red** | Enrutamiento y direccionamiento lógico (IP) | IP, ICMP, ARP, OSPF | Paquete |
| **2** | 🔌 **Enlace de Datos** | Comunicación entre nodos adyacentes, MAC addresses | Ethernet, Wi-Fi, PPP | Trama (Frame) |
| **1** | ⚡ **Física** | Transmisión de bits por el medio físico | Cables, fibra óptica, señales eléctricas | Bits |

---

## 🔍 Detalle de Cada Capa

### Capa 7 — Aplicación 🖥️
> Es la capa más cercana al **usuario**. Aquí operan los protocolos que usamos directamente.
- **HTTP/HTTPS** → Navegación web
- **FTP** → Transferencia de archivos
- **SSH** → Acceso remoto seguro
- **DNS** → Resolución de nombres de dominio
- **SMTP** → Envío de correos electrónicos

### Capa 6 — Presentación 🔤
> Se encarga de **traducir** los datos a un formato que la capa de aplicación pueda entender.
- Cifrado y descifrado (SSL/TLS)
- Compresión de datos
- Conversión de formatos (ASCII, JPEG, etc.)

### Capa 5 — Sesión 🔗
> Gestiona las **sesiones** de comunicación entre dos dispositivos.
- Establece, mantiene y termina conexiones
- Controla el diálogo (quién transmite y cuándo)
- Sincronización de datos

### Capa 4 — Transporte 🚛
> Garantiza la entrega de datos **extremo a extremo**.
- **TCP** → Orientado a conexión, fiable (Three-Way Handshake)
- **UDP** → Sin conexión, más rápido pero sin garantía

> 💡 **Para hacking:** Esta capa es clave para entender escaneos de puertos (Nmap) y cómo funcionan los servicios.

### Capa 3 — Red 🗺️
> Se encarga del **enrutamiento** — decidir por dónde viajan los paquetes.
- Direccionamiento IP (IPv4, IPv6)
- Los **routers** operan en esta capa
- Subnetting y cálculo de rutas

### Capa 2 — Enlace de Datos 🔌
> Comunicación entre dispositivos en la **misma red local**.
- Direcciones **MAC** (Media Access Control)
- Los **switches** operan en esta capa
- Detección de errores en tramas

### Capa 1 — Física ⚡
> El medio **físico** por donde viajan los bits.
- Cables de red (Ethernet, fibra óptica)
- Señales eléctricas, ópticas o de radio
- Conectores, hubs, repetidores

---

## 💡 Regla Mnemotécnica

Para recordar las capas de **abajo hacia arriba** (1→7):

> **"Please Do Not Throw Sausage Pizza Away"**
> 
> Physical → Data Link → Network → Transport → Session → Presentation → Application

---

## 🎯 Relevancia en Hacking

```
Capa 7 (Aplicación)   → Ataques web (SQLi, XSS), phishing
Capa 4 (Transporte)   → Escaneo de puertos, SYN flood (DoS)
Capa 3 (Red)           → Spoofing de IP, sniffing, MITM
Capa 2 (Enlace)        → ARP Spoofing, MAC flooding
Capa 1 (Física)        → Acceso físico, sniffing de cables
```




