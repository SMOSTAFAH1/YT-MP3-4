import sys

def main():
    """Función principal."""
    if len(sys.argv) < 3:
        print("Uso: python YT.py <URL> <opcion>")
        print("Ejemplo: python YT.py https://www.youtube.com/watch?v=dQw4w9WgXcQ 1")
        return

    url = sys.argv[1]
    opcion = sys.argv[2]

    if opcion in ('1', '2'):
        descargar(url, 'video' if opcion == '1' else 'audio')
    else:
        print("Opción inválida")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nPrograma terminado") 