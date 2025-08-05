import requests
from PIL import Image
from Obras import Obras

def obtener_departamentos():
    url = "https://collectionapi.metmuseum.org/public/collection/v1/departments"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["departments"]

def obtener_ids_por_departamento(dept_id):
    url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects?departmentIds={dept_id}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["objectIDs"][:10]

def obtener_detalle_obra(object_id):
    url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{object_id}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return Obras(
        object_id=data["objectID"],
        title=data.get("title", "N/A"),
        artist_name=data.get("artistDisplayName", "N/A"),
        nationality=data.get("artistNationality", "N/A"),
        object_date=data.get("objectDate", "N/A"),
        classification=data.get("classification", "N/A"),
        image_url=data.get("primaryImage", "")
    )

def guardar_y_mostrar_imagen(url, nombre_archivo):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        extension = ".jpg" if "jpeg" in response.headers.get("Content-Type", "") else ".png"
        nombre_final = f"{nombre_archivo}{extension}"
        with open(nombre_final, "wb") as f:
            for chunk in response.iter_content(8192):
                f.write(chunk)
        img = Image.open(nombre_final)
        img.show()
    except Exception as e:
        print(f"Error al mostrar imagen: {e}")

def cargar_nacionalidades(archivo="nacionalidades.txt"):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("Archivo de nacionalidades no encontrado.")
        return []

def buscar_obras_por_nacionalidad(nacionalidad, cantidad=20):
    url = f"https://collectionapi.metmuseum.org/public/collection/v1/search?artistNationality={nacionalidad}&hasImages=true&q=*"
    response = requests.get(url)
    response.raise_for_status()
    ids = response.json().get("objectIDs", [])[:cantidad]
    return [obtener_detalle_obra(oid) for oid in ids]

def buscar_obras_por_autor(nombre_autor, cantidad=20):
    url = f"https://collectionapi.metmuseum.org/public/collection/v1/search?q={nombre_autor}&hasImages=true"
    response = requests.get(url)
    response.raise_for_status()
    ids = response.json().get("objectIDs")

    obras_filtradas = []
    for oid in ids:
        obra = obtener_detalle_obra(oid)
        if obra and nombre_autor.lower() in obra.artist_name.lower():
            obras_filtradas.append(obra)
            if len(obras_filtradas) >= cantidad:
                break
    return obras_filtradas