class obras:
    def __init__(self, id_objeto, titulo, artista, nacionalidad, fecha_objeto, clasificacion, url):
        """"Pasando los argumentos necesarios para la clase obras"""
        self.id_objeto= id_objeto
        self.titulo= titulo
        self.artista= artista
        self.nacionalidad= nacionalidad
        self.fecha_objeto= fecha_objeto
        self.clasificacion= clasificacion
        self.url= url

    def show (self):
        """"Imprime la imformacion necesaria de la obra"""
        print(f"ID: {self.id_objeto}")
        print(f"Titulo: {self.titulo}")
        print(f"Artista: {self.artista}")
        print(f"nacionalidad: {self.nacionalidad}")
        print(f"Fecha objeto: {self.fecha_objeto}")
        print(f"Clasificacion: {self.clasificacion}")
        if self.url:
            print(f"Imagen: {self.url}")
        print()

    def mostrar_info(self):
        """"Retorna la informacion basica de ID, titulo y nombre del artista"""

        return f"ID: {self.id_objeto} - Titulo: {self.titulo} - Artista: {self.artista}"