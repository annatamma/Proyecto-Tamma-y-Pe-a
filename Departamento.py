class Departamento:
    def __init__(self, id_departamento, nombre):
        """"Pasando los argumentos necesarios para la clase Departamento"""
        self.id_departamento= id_departamento
        self.nombre= nombre

    def show (self):
        """Imprime la imformacion de la clase departamento"""
        print(f"ID departamento: {self.id_departamento}")
        print(f"Nombre: {self.nombre}")
        print()