class Estadisticas:
    def __init__(self, data):
        self.temporadas = data["temporadas"]
        self.puntos_totales = data["puntos_totales"]
        self.promedio_puntos_por_partido = data["promedio_puntos_por_partido"]
        self.rebotes_totales = data["rebotes_totales"]
        self.promedio_rebotes_por_partido = data["promedio_rebotes_por_partido"]
        self.asistencias_totales = data["asistencias_totales"]
        self.promedio_asistencias_por_partido = data["promedio_asistencias_por_partido"]
        self.robos_totales = data["robos_totales"]
        self.bloqueos_totales = data["bloqueos_totales"]
        self.porcentaje_tiros_de_campo = data["porcentaje_tiros_de_campo"]
        self.porcentaje_tiros_libres = data["porcentaje_tiros_libres"]
        self.porcentaje_tiros_triples = data["porcentaje_tiros_triples"]