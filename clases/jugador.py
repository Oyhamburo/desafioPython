from clases.estadisticas import Estadisticas

class Jugador:
    def __init__(self, data):
        self.nombre = data["nombre"]
        self.posicion = data["posicion"]
        self.estadisticas = Estadisticas(data["estadisticas"])
        self.logros = data["logros"]
