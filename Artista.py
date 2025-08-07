class Artista:
    """La clase no se uso pero se elaboro por si se necesitaba utilizar"""
    def __init__(self, nombre, nacionalidad, fecha_nacimiento, fecha_fallecimiento):
        """"Pasando los argumentos necesarios para la clase Artista"""
        self.nombre= nombre
        self.nacionalidad= nacionalidad
        self.fecha_nacimiento= fecha_nacimiento
        self.fecha_fallecimiento= fecha_fallecimiento

    def show (self):
        """Imprime la imformacion de la clase artista"""
        print(f"Nombre: {self.nombre}")
        print(f"Nacionalidad: {self.nacionalidad}")
        print(f"Fecha nacimiento: {self.fecha_nacimiento}")
        print(f"Fecha fallecimiento: {self.fecha_fallecimiento}")

    