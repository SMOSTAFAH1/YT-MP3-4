import yt_dlp
import os
from typing import Literal

def get_download_options(content_type: Literal['video', 'audio']) -> dict:
    """Retorna opciones de descarga según el tipo de contenido."""
    base_path = f'downloads/{content_type}s'
    os.makedirs(base_path, exist_ok=True)
    
    opts = {
        'format': 'bestvideo+bestaudio/best' if content_type == 'video' else 'bestaudio/best',
        'outtmpl': f'{base_path}/%(title)s.%(ext)s',
        'http_headers': {'User-Agent': 'Mozilla/5.0'}
    }
    
    if content_type == 'audio':
        opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'
        }]
        
    return opts

def descargar(url: str, tipo: Literal['video', 'audio']) -> None:
    """Descarga contenido desde URL."""
    if not url.strip():
        print("Error: URL vacía")
        return
        
    try:
        with yt_dlp.YoutubeDL(get_download_options(tipo)) as ydl:
            print(f"Descargando {tipo}...")
            ydl.download([url])
            print(f"¡{tipo.capitalize()} descargado!")
    except Exception as e:
        print(f"Error: {str(e)}")

def main():
    """Función principal."""
    while True:
        url = input("\nURL del video (q para salir): ").strip()
        if url.lower() == 'q':
            break
            
        opcion = input("1. Video MP4\n2. Audio MP3\nElige (1/2): ").strip()
        
        if opcion in ('1', '2'):
            descargar(url, 'video' if opcion == '1' else 'audio')
        else:
            print("Opción inválida")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nPrograma terminado")
