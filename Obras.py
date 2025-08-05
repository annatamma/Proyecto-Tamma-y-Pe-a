class Obra:
    def __init__(self, id_objeto, titulo, artista, id_departamento, nacionalidad, fecha_objeto, clasificacion, url):
        self.id_objeto= id_objeto
        self.titulo= titulo
        self.artista= artista
        self.id_departamento= id_departamento
        self.nacionalidad= nacionalidad
        self.fecha_objeto= fecha_objeto
        self.clasrificacion= clasificacion
        self.url= url

    def show (self):
        print(f"ID objeto: {self.id_objeto}")
        print(f"Titulo: {self.titulo}")
        print(f"Artista: {self.artista}")
