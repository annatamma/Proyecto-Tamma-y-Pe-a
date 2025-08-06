def obtener_nacionalidades_de_archivo(archivo):
    """Lee una lista de nacionalidades de un archivo CSV"""
    nacionalidades = []

    try:
        with open(archivo, "r") as file:
            for line in file:
                nacionalidades.append(line)
    except Exception:
        print("Ocurrió un error al cargar el archivo.")
    return nacionalidades