import requests
from Obras import obras
from Departamento import Departamento
from PIL import Image

def obtener_departamentos():
    url = "https://collectionapi.metmuseum.org/public/collection/v1/departments"
    response = requests.get(url)
    response.raise_for_status()
    departamentos_dict = response.json()["departments"]
    departamentos = []
    for dic in departamentos_dict:
        departamentos.append(Departamento(id_departamento=dic["departmentId"], nombre=dic["displayName"]))
    return departamentos


def obtener_ids_por_departamento(dept_id):
    url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects?departmentIds={dept_id}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["objectIDs"] 

#print(obtener_ids_por_departamento(15))

def obtener_detalle_obra(object_id):
    """
    Obtiene los detalles de una obra específica desde la API del Met.
    Maneja errores 404 (no encontrado) y 403 (prohibido/límite de tasa).
    """
    url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{object_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return obras(
            id_objeto=data.get("objectID"),
            titulo=data.get("title"),
            artista=data.get("artistDisplayName"),
            nacionalidad=data.get("artistNationality"),
            fecha_objeto=data.get("objectDate"),
            clasificacion=data.get("classification"),
            url=data.get("primaryImage", "")
        )
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print(f"Advertencia: Objeto con ID {object_id} no encontrado (404). Saltando este objeto.")
            return None
        elif e.response.status_code == 403:
            print(f"ERROR: 403 Forbidden para el objeto {object_id}. Límite de tasa de la API excedido.")
            print("No se pueden obtener más detalles en este momento para evitar bloqueos.")
            
        else:
            print(f"Error HTTP inesperado {e.response.status_code} para el objeto {object_id}: {e}. Saltando este objeto.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión o solicitud para el objeto {object_id}: {e}. Saltando este objeto.")
        return None


def guardar_imagen(url, nombre_archivo):
    if not url:
        print("URL de imagen no proporcionada.")
        return None
    

    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  

        content_type = response.headers.get('Content-Type', '')
        extension = '.jpg'  # Valor por defecto
        if 'image/png' in content_type:
            extension = '.png'
        elif 'image/jpeg' in content_type:
            extension = '.jpg'
        elif 'image/svg+xml' in content_type:
            extension = '.svg'
        
        

        nombre_archivo_final = f"{nombre_archivo}{extension}"
        

        with open(nombre_archivo_final, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Imagen guardada exitosamente como '{nombre_archivo_final}'")
        return nombre_archivo_final 
    except Exception as e:
        print(f"Error al mostrar imagen: {e}")



def mostrar_imagen(ruta_imagen):
    try:
        img = Image.open(ruta_imagen)
        img.show() # Abre la imagen en el visor de imágenes predeterminado del sistema
        print(f"Mostrando imagen: '{ruta_imagen}'")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo de imagen en '{ruta_imagen}'.")
    except Exception as e:
        print(f"Error al intentar mostrar la imagen '{ruta_imagen}': {e}")



def buscar_obras_por_nacionalidad(nacionalidad, lista_obras):
    resultado=[]
    for obra in lista_obras:
        if obra.nacionalidad.lower()==nacionalidad.lower():
            resultado.append(obra)
    return resultado



def buscar_obras_por_nac(nacionalidad, cantidad=20):
    url = f"https://collectionapi.metmuseum.org/public/collection/v1/search?artistOrCulture=true&q={nacionalidad}"
    response = requests.get(url)
    response.raise_for_status()
    ids = response.json().get("objectIDs", [])

    obras_filtradas = []
    for oid in ids:
        obra = obtener_detalle_obra(oid)
        if obra and nacionalidad.lower() == obra.nacionalidad.lower():
            obras_filtradas.append(obra)
            if len(obras_filtradas) >= cantidad:
                break
    return obras_filtradas



def buscar_obras_por_autor(nombre_autor, cantidad=20):
    url = f"https://collectionapi.metmuseum.org/public/collection/v1/search?q={nombre_autor}&hasImages=true"
    response = requests.get(url)
    response.raise_for_status()
    ids = response.json().get("objectIDs", [])[:100]

    obras_filtradas = []
    for oid in ids:
        obra = obtener_detalle_obra(oid)
        if obra and nombre_autor.lower() in obra.artista.lower():
            obras_filtradas.append(obra)
            if len(obras_filtradas) >= cantidad:
                break
    return obras_filtradas
