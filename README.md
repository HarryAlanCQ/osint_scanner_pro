# 🕵️‍♂️ OSINT Scanner Pro – v1.0

Herramienta básica escrita en Python para realizar reconocimiento pasivo de dominios públicos mediante técnicas de OSINT (Open Source Intelligence).

---

## 🚀 Funcionalidades

- ✅ Obtener la IP asociada a un dominio
- ✅ Ver las cabeceras HTTP del servidor web
- ✅ Generar reportes automáticos con IP + cabeceras en formato `.txt`
- ✅ Menú interactivo desde consola
- ✅ Manejo de errores si el dominio no existe o el servidor no responde

---

## 🧪 Tecnologías usadas

- Python 3.10+
- `socket` (para resolución DNS)
- `requests` (para peticiones HTTP)
- `datetime` (para timestamp de reportes)
- `os` (limpieza visual en consola)

---

## 🖥️ Captura de ejemplo

Introduce el dominio: google.com

BIENVENIDO AL MENÚ DE OPCIONES

1. Obtener IP del dominio
2. Ver cabeceras HTTP del sitio
3. Hacer ambas y guardar en reporte
4. Salir

---

## 📁 Estructura recomendada del proyecto

osint_scanner/
├── osint_scanner.py
├── README.md
├── /reportes/
│ ├── google.com_2025-07-16_14-30.txt
│ └── ...
└── requirements.txt

---

## ✅ Cómo usarlo

1. Clona el proyecto:
```bash
git clone https://github.com/HarryAlanCQ/osint_scanner.git
cd osint_scanner
