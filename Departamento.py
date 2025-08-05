class Departamento:
    def __init__(self, id_departamento, nombre):
        self.id_departamento= id_departamento
        self.nombre= nombre

    def show (self):
        print(f"ID departamento: {self.id_departamento}")
        print(f"Nombre: {self.nombre}")
        