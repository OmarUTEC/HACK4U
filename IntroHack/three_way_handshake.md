# 🤝 Three-Way Handshake — Establecimiento de Conexión TCP

---

## 📡 Protocolos de Transporte (Capa 4 — OSI)

| Protocolo | Tipo | Handshake | Fiabilidad | Uso típico |
|-----------|------|-----------|------------|------------|
| **TCP** | Orientado a conexión | ✅ Three-Way Handshake | Garantiza entrega ordenada | HTTP, SSH, FTP, SMTP |
| **UDP** | Sin conexión | ❌ No tiene | No garantiza entrega | DNS, DHCP, VoIP, streaming |

---

## 🔄 ¿Qué es el Three-Way Handshake?

Es el proceso de **3 pasos** que TCP utiliza para establecer una conexión fiable entre un **cliente** y un **servidor** antes de transmitir datos. Se conoce coloquialmente como el **"apretón de manos"**.

---

## 📊 Diagrama del Proceso

```
     Cliente                              Servidor
        │                                    │
        │  ──── 1. SYN ──────────────►       │   "¿Puedo conectarme?"
        │                                    │
        │  ◄──── 2. SYN + ACK ────────       │   "Sí, adelante"
        │                                    │
        │  ──── 3. ACK ──────────────►       │   "Perfecto, conectados"
        │                                    │
        │  ═══════ CONEXIÓN ESTABLECIDA ═════│
        │         (datos fluyen aquí)        │
        │                                    │
```

---

## 📝 Explicación Paso a Paso

### Paso 1 — `SYN` (Synchronize)
> El **cliente** envía un paquete `SYN` al servidor para solicitar una conexión.

### Paso 2 — `SYN/ACK` (Synchronize + Acknowledge)
> El **servidor** responde con un paquete `SYN/ACK` indicando que acepta la conexión.

### Paso 3 — `ACK` (Acknowledge)
> El **cliente** confirma con un `ACK`. La conexión queda en estado **ESTABLISHED** y los datos pueden fluir.

---

## ❌ ¿Qué pasa si el puerto está cerrado?

```
     Cliente                              Servidor
        │                                    │
        │  ──── SYN ─────────────────►       │
        │                                    │
        │  ◄──── RST ────────────────        │   "Puerto cerrado, rechazado"
        │                                    │
```

> Si el puerto está **cerrado**, el servidor responde con un paquete `RST` (Reset) en lugar de `SYN/ACK`.

---

## 🆚 TCP vs UDP — Resumen Visual

```
  TCP (Conexión fiable)              UDP (Sin conexión)
  ┌─────────────────────┐           ┌─────────────────────┐
  │  SYN ──────►        │           │                     │
  │  ◄────── SYN/ACK    │           │  Datos ──────►      │
  │  ACK ──────►        │           │  Datos ──────►      │
  │  ═══ Datos ═══      │           │  Datos ──────►      │
  │  (ordenados)        │           │  (sin garantía)     │
  └─────────────────────┘           └─────────────────────┘
```

> 💡 **TCP** es como enviar una carta certificada (sabes que llegó). **UDP** es como gritar en una habitación (esperas que alguien escuche, pero no lo verificas).



