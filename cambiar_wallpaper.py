#!/usr/bin/env python3

import os
import random
import subprocess
import time

carpeta_imagenes = "/home/chrysdeb/Imágenes/Wallpapers"  # Ajusta la ruta
log_file = "/home/chrysdeb/cron_log.txt"

def log(message):
    with open(log_file, "a") as f:
        f.write(f"{message}\n")

extensiones_validas = (".jpg", ".jpeg", ".png", ".bmp")
imagenes = [f for f in os.listdir(carpeta_imagenes) if f.lower().endswith(extensiones_validas)]

if not imagenes:
    log(f"No se encontraron imágenes en {carpeta_imagenes}")
    exit(1)

while True:
    imagen_aleatoria = random.choice(imagenes)
    ruta_completa = os.path.join(carpeta_imagenes, imagen_aleatoria)
    comando = f"gsettings set org.gnome.desktop.background picture-uri 'file://{ruta_completa}'"
    try:
        subprocess.run(comando, shell=True, check=True)
        log(f"Éxito: Fondo cambiado a {imagen_aleatoria}")
    except subprocess.CalledProcessError as e:
        log(f"Error al ejecutar gsettings: {e}")
    time.sleep(180)  # 180 segundos = 3 minutos
