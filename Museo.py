from Obras import obras
from api import obtener_departamentos,obtener_ids_por_departamento, obtener_detalle_obra, guardar_imagen, mostrar_imagen, buscar_obras_por_nacionalidad, buscar_obras_por_autor
from nacionalidades import obtener_nacionalidades_de_archivo

class Museo:
    def __init__(self, api=None, obras_arte=None):
        """Inicializa la clase Museo"""
        self.api= api
        
    def solicitar_departamentos(self, start=0, end=20):
        """Permite al usuario elegir un departamento
         Le proporciona al usuario una informacion basica de la obras por ese departamento y limita las consultas de las obras de la API de 20 en 20 """
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
        """Permite al usuario ver todos los detalles de la obra seleccionada
        Tambien muestra la opcion de ver la imagen de la obra si esta disponible"""
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
            """Es el menu de las opciones que el usuario puede seleccionar"""

            while True:
                menu=input("""Bienvenido a MetroArt. Elija una opcion:
    1- Mostrar obras por departamento
    2- Mostrar por nacionalidad del autor
    3- Mostrar obras por nombre del autor
    4- Salir

    --->""")
                if menu=="1":
                    self.solicitar_departamentos()
                    self.ver_detalles()
                
                elif menu=="2":
                    self.cargar_nacionalidades()
                    self.ver_detalles()
                
                elif menu=="3":
                    self.buscar_obras_por_autor()
                    self.ver_detalles()
      
                elif menu=="4":
                    print("Gracias por su visita")
                    break
                else:
                     print("Error. Vuelva a intentar")


    def cargar_nacionalidades(self):
        """Carga una lista de las nacionalidades
         Permite al usuario seleccior una y de esa manera arrojar las obras de la nacionalidad escogida"""
        nacionalidades = obtener_nacionalidades_de_archivo("archivo_nacionalidades.csv")
        self.obras_arte = []
        for i, n in enumerate(nacionalidades): 
            print(f"{i+1}. {n}")
        seleccion = input("Seleccione el número de la nacionalidad: ")
        try:
            idx = int(seleccion) - 1
            if 0 <= idx < len(nacionalidades):
                obras = buscar_obras_por_nacionalidad(nacionalidades[idx])
                for obra in obras:
                    if obra:
                        self.obras_arte.append(obra)
                        print(obra.mostrar_info())
            else:
                print("Selección inválida.")
        except ValueError:
            print("Entrada no válida.")

    
    def buscar_obras_por_autor(self):
        """Permite al usurio buscar obras por el nombre del autor"""
        self.obras_arte = []
        nombre_autor = input("Ingrese el nombre del autor: ")
        if nombre_autor:
            self.obras_arte = buscar_obras_por_autor(nombre_autor)
            if self.obras_arte:
                for obra in self.obras_arte:
                    print(obra.mostrar_info())
            else:
                print("No se encontraron obras para ese autor.")
        else:
            print("Debe ingresar un nombre.")

