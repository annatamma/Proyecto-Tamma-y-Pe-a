from Obras import obras
from api import obtener_departamentos,obtener_ids_por_departamento, obtener_detalle_obra, guardar_imagen, mostrar_imagen, buscar_obras_por_nacionalidad, buscar_obras_por_autor
from nacionalidades import obtener_nacionalidades_de_archivo

class Museo:
    def __init__(self, api=None, obras_arte=None):
        self.api= api
        
    def solicitar_departamentos(self, start=0, end=20):
        departamentos = obtener_departamentos()
        for d in departamentos:
            d.show()

        departamento_id = input("Ingrese el ID del departamento que desea consultar: ")
        ids = obtener_ids_por_departamento(int(departamento_id))

        self.obras_arte = []
        while True:

            for i in ids[start:end]:
                obra = obtener_detalle_obra(i)
                if obra: 
                    self.obras_arte.append(obra)
                    print(obra.mostrar_info())
                else:
                    break
        
            mostrar= input("Límite de consultas alcanzado. Debe esperar un minuto. ¿Desea mostrar los demás resultados? \n1. Si, 2. No  -->")
            if mostrar == "2":
                break
            else:
                if len(ids)>end:
                    start= end + 1
                if len(ids)>= end + 20: 
                    end = start + 20
                else:
                    end=len(ids)-1

    def ver_detalles(self):
        obra_id = input("\nIngrese el ID de la obra para ver detalles: ")
        seleccionada = None
        for o in self.obras_arte:
            if str(o.id_objeto) == obra_id:
                seleccionada = o
        if seleccionada:
            seleccionada.show()
            if seleccionada.url:
                ver = input("¿Desea ver la imagen? (s/n): ")
                if ver.lower() == "s":
                    foto = guardar_imagen(seleccionada.url, seleccionada.titulo)
                    mostrar_imagen(foto)
                    pass
        else:
            print("Obra no encontrada.")
        
    def start(self):

            while True:
                menu=input("""Bienvenido a MetroArt. Elija una opcion:
    1- Mostrar obras por departamento
    2- Mostrar por nacionalidad del autor
    3- Mostrar obras por nombre del autor
    4- Salir

    --->""")
                if menu=="1":
                    
                    pass
                
                elif menu=="2":
                    pass
                elif menu=="3":
                    pass

                        
                elif menu=="4":
                    break
                else:
                     print("Error. Vuelva a intentar")


    def solicitar_departamentos(self):
        departamentos = obtener_departamentos()
        for d in departamentos:
            print(f"{'Id'}: {"nombre"}")

        departamento_id = input("Ingrese el ID del departamento que desea consultar: ")
        ids = obtener_ids_por_departamento(departamento_id)

        obras = []
        for i in ids:
            obra = obtener_detalle_obra(i)

        obras.append(obra)
        print(obra.mostrar_info_basica())

        obra_id = input("\nIngrese el ID de la obra para ver detalles: ")
        seleccionada = ((o for o in obras if str(o.object_id) == obra_id), None)
        if seleccionada:
            seleccionada.mostrar_detalles()
        if seleccionada.image_url:
            ver = input("¿Desea ver la imagen? (s/n): ")
        if ver.lower() == "s":
            #guardar_y_mostrar_imagen(seleccionada.image_url, f"obra_{seleccionada.object_id}")  
            pass
        else:
            print("Obra no encontrada.")


    def cargar_nacionalidades(self):
        nacionalidades = obtener_nacionalidades_de_archivo()
        for i, n in enumerate(nacionalidades):
            print(f"{i+1}. {n}")
        seleccion = input("archivo_nacionalidades.csv")
        try:
            idx = int(seleccion) - 1
            if 0 <= idx < len(nacionalidades):
                obras = buscar_obras_por_nacionalidad(nacionalidades[idx])
                for obra in obras:
                    print(obra.mostrar_info_basica())
            else:
                print("Selección inválida.")
        except ValueError:
            print("Entrada no válida.")

    
    def buscar_obras_por_autor(self):

        nombre_autor = input("Ingrese el nombre del autor: ")
        if nombre_autor:
            obras = buscar_obras_por_autor(nombre_autor)
            if obras:
                for obra in obras:
                    print(obra.mostrar_info())
            else:
                print("No se encontraron obras para ese autor.")
        else:
            print("Debe ingresar un nombre.")

