import tkinter as tk
from tkinter import messagebox, ttk
import yt_dlp
#import os
from pathlib import Path

# Función para descargar el video
def descargar_video():
    url = entry_url.get()
    
    if not url.strip():
        messagebox.showerror("Error", "La URL no puede estar vacía.")
        return
    
    try:
        # Obtener la ruta del escritorio del usuario
        escritorio = Path.home() / "Desktop" / "BlaizeTube"
        
        # Crear la carpeta si no existe
        if not escritorio.exists():
            escritorio.mkdir(parents=True)
        
        # Ruta de salida para los videos descargados
        ruta_salida = str(escritorio / "%(title)s.%(ext)s")
        
        # Agregar la opción para no descargar toda la lista de reproducción
        ydl_opts = {
            'outtmpl': ruta_salida,  # Guardar en la carpeta BlaizeTube
            'noplaylist': True,  # Esta opción evita la descarga de la lista de reproducción
            'progress_hooks': [actualizar_progreso]
        }
        
        # Crear una instancia de YoutubeDL con las opciones configuradas
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        messagebox.showinfo("Éxito", f"Descarga completada en {escritorio}")
    
    except yt_dlp.utils.DownloadError as e:
        messagebox.showerror("Error de descarga", f"Ocurrió un error durante la descarga: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"Ha ocurrido un error inesperado: {e}")

# Función para actualizar la barra de progreso y mostrar el tiempo restante
def actualizar_progreso(d):
    if d['status'] == 'downloading':
        progreso = d['downloaded_bytes'] / d['total_bytes'] * 100
        barra_progreso['value'] = progreso
        
        # Actualiza el tiempo restante
        tiempo_restante.set(f"Tiempo restante: {format_tiempo(d['eta'])}")
        ventana.update_idletasks()  # Actualiza la interfaz en cada paso
    
    elif d['status'] == 'finished':
        barra_progreso['value'] = 100
        tiempo_restante.set("Descarga completada.")

# Función para formatear el tiempo restante
def format_tiempo(segundos):
    if segundos is None:
        return "Calculando..."
    minutos, segundos = divmod(segundos, 60)
    return f"{int(minutos)}m {int(segundos)}s"

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("BlaizeTube - Descargador de Videos de YouTube")
ventana.geometry("500x350")  # Ajustar tamaño de ventana para más espacio
ventana.resizable(False, False)  # Impide que la ventana sea redimensionable

# Establecer el color de fondo
ventana.config(bg='#f0f0f0')

# Título de la aplicación
titulo = tk.Label(ventana, text="BlaizeTube", font=("Arial", 16, "bold"), bg='#f0f0f0', fg='#333')
titulo.pack(pady=10)

# Crear y colocar la etiqueta
etiqueta = tk.Label(ventana, text="Introduce la URL del video de YouTube:",
                     font=("Arial", 12), bg='#f0f0f0')
etiqueta.pack(pady=5)

# Crear el campo de entrada para la URL
entry_url = tk.Entry(ventana, width=40, font=("Arial", 12))
entry_url.pack(pady=5)

# Crear el botón para iniciar la descarga
boton_descargar = ttk.Button(ventana, text="Descargar Video", command=descargar_video)
boton_descargar.pack(pady=10)

# Crear la barra de progreso
barra_progreso = ttk.Progressbar(ventana, orient="horizontal", length=400, mode="determinate")
barra_progreso.pack(pady=10)

# Crear el texto que muestra el tiempo restante
tiempo_restante = tk.StringVar()
tiempo_label = tk.Label(ventana, textvariable=tiempo_restante, font=("Arial", 10), bg='#f0f0f0')
tiempo_label.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()
