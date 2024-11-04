import pyautogui
import random
import time
from datetime import datetime, timedelta
import subprocess

def abrir_zoom():
    try:
        # Cambia la ruta a la de tu instalación de Zoom en Windows.
        subprocess.Popen("C:\\Path\\To\\Zoom\\zoom.exe")  
        time.sleep(5)  # Espera a que Zoom se abra
    except Exception as e:
        print(f"Error al abrir Zoom: {e}")

def maximizar_zoom():
    zoom_window = pyautogui.getWindowsWithTitle("Zoom")
    if zoom_window:
        window = zoom_window[0]
        if not window.isMaximized:
            window.maximize()
    else:
        print("No se encontró la ventana de Zoom. Intentando abrir Zoom...")
        abrir_zoom()

def generar_horas_aleatorias(inicio="18:00", fin="22:00", cantidad=3):
    formato = "%H:%M"
    hora_inicio = datetime.strptime(inicio, formato)
    hora_fin = datetime.strptime(fin, formato)
    horas_aleatorias = set()
    
    while len(horas_aleatorias) < cantidad:
        random_segundos = random.randint(0, int((hora_fin - hora_inicio).total_seconds()))
        nueva_hora = (hora_inicio + timedelta(seconds=random_segundos)).time()
        horas_aleatorias.add(nueva_hora)
    
    return sorted(list(horas_aleatorias))

def tomar_captura(nombre_archivo):
    captura = pyautogui.screenshot()
    captura.save(nombre_archivo)
    print(f"Captura guardada como {nombre_archivo}")

def main():
    # Generar tres horas aleatorias entre 6 p.m. y 10 p.m.
    horas_capturas = generar_horas_aleatorias()
    print(f"Horarios de capturas: {horas_capturas}")
    
    # Comienza a revisar cada hora generada
    for hora in horas_capturas:
        while datetime.now().time() < hora:
            time.sleep(10)  # Esperar un tiempo antes de verificar nuevamente
        
        # Maximizar la ventana de Zoom si está abierta, o abrirla si no está
        maximizar_zoom()
        
        # Tomar la captura de pantalla
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        tomar_captura(f"captura_zoom_{timestamp}.png")
    
    print("Capturas completadas.")

if __name__ == "__main__":
    main()
