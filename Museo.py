from Obras import Obras
from api import obtener_departamentos,obtener_ids_por_departamento, obtener_detalle_obra, guardar_y_mostrar_imagen, cargar_nacionalidades, buscar_obras_por_nacionalidad, buscar_obras_por_autor

class Museo:
    def __init__(self, api):
        self.api= api
        
def start(self):

        while True:
            menu=input("""Bienvenido a MetroArt. Elija una opcion:
1- Mostrar obras por departamento
2- Mostrar por nacionalidad del autor
3- Mostrar obras por nombre del autor
4- Salir

--->""")
            if menu=="1":
                self.obtener_departamentos()
            
            elif menu=="2":
                self.cargar_nacionalidades()
            
            elif menu=="3":
                self.buscar_obras_por_autor()
                    
            elif menu=="4":
                break


        def obtener_departamentos(self):
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
            guardar_y_mostrar_imagen(seleccionada.image_url, f"obra_{seleccionada.object_id}")
        else:
            print("Obra no encontrada.")


        def cargar_nacionalidades(self):
            nacionalidades = cargar_nacionalidades()
            for i, n in enumerate(nacionalidades):
                print(f"{i+1}. {n}")
            seleccion = input("Seleccione el número de la nacionalidad: ")
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

    