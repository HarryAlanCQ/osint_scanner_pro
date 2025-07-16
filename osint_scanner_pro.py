import os
import socket
import requests
from datetime import datetime

os.system('cls')

dominio = input('Introduce el dominio: ')

def obtener_ip(dominio):
    try:
        ip = socket.gethostbyname(dominio)
        print(f"La IP de {dominio} es {ip}")
        return ip
    except socket.gaierror:
        print(f"No se pudo resolver el dominio: {dominio}")
        return None

def obtener_cabeceras(dominio):
    url = f'https://{dominio}'
    headers = {
       "User-Agent": "Mozilla/5.0 (AlanBot 1.0)"
    }
    try:
        cabeceras = requests.get(url, headers=headers, timeout=5)

        texto = 'CABECERAS DEL SERVIDOR:\n'
        for clave, valor in cabeceras.headers.items():
            texto += (f"\n{clave}: {valor}")
        print(texto)
        return texto
    except requests.exceptions.RequestException as e:
        print(f"Error al conectarse a {url}: {e}")
        return "No se pudo obtener cabeceras"

def ambas_en_reporte(dominio):

    ip = obtener_ip(dominio)
    if ip is None:
        print("No se puede generar el reporte con una ip válida")
        return
    
    texto = obtener_cabeceras(dominio)
    fecha = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    archivo = f"{dominio}_{fecha}.txt"

    with open(f"../Desktop/{archivo}", "w") as f:
        f.write(f'Reporte de OSINT para: {dominio}\n')
        f.write(f'IP: {ip}\n')
        f.write(texto)

    print('¡Se realizó con éxito!')

while True:
    print(f"""
    BIENVENIDO AL MENÚ DE OPCIONES
          
1. Obtener IP del dominio
2. Ver cabeceras HTTP del sitio
3. Hacer ambas y guardar en reporte
4. Salir
          """)
          
    opcion = int(input('Introduce una opción: '))

    if opcion == 1:
        os.system('cls')
        obtener_ip(dominio)

    elif opcion == 2:
        os.system('cls')
        obtener_cabeceras(dominio)

    elif opcion == 3:
        os.system('cls')
        ambas_en_reporte(dominio)

    elif opcion == 4:
        break
    else:
        print('Opción no válida. Saliendo del programa...')
        break