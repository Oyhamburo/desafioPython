import json
from clases.jugador import Jugador

class Equipo:
    def __init__(self, json_file):
        self.jugadores = []
        self.load_data_from_json(json_file)

    def load_data_from_json(self, json_file):
        try:
            with open(json_file, "r") as file:
                data = json.load(file)
                if "equipo" in data and "jugadores" in data:
                    for jugador_data in data["jugadores"]:
                        jugador = Jugador(jugador_data)
                        self.jugadores.append(jugador)
                else:
                    print("El archivo JSON no tiene el formato esperado.")
        except FileNotFoundError:
            print(f"El archivo JSON '{json_file}' no se encontró.")

    def list_players(self):
        for jugador in self.jugadores:
            print(f"{jugador.nombre} - {jugador.posicion}")

    def get_player_stats(self, index):
        if 0 <= index < len(self.jugadores):
            jugador = self.jugadores[index]
            print(f"Estadísticas de {jugador.nombre}:")
            print(f"Temporadas jugadas: {jugador.estadisticas.temporadas}")
            print(f"Puntos totales: {jugador.estadisticas.puntos_totales}")
            print(f"Promedio de puntos por partido: {jugador.estadisticas.promedio_puntos_por_partido}")
            print(f"Rebotes totales: {jugador.estadisticas.rebotes_totales}")
            print(f"Promedio de rebotes por partido: {jugador.estadisticas.promedio_rebotes_por_partido}")
            print(f"Asistencias totales: {jugador.estadisticas.asistencias_totales}")
            print(f"Promedio de asistencias por partido: {jugador.estadisticas.promedio_asistencias_por_partido}")
            print(f"Robos totales: {jugador.estadisticas.robos_totales}")
            print(f"Bloqueos totales: {jugador.estadisticas.bloqueos_totales}")
            print(f"Porcentaje tiros de campo: {jugador.estadisticas.porcentaje_tiros_de_campo}%")
            print(f"Porcentaje tiros libres: {jugador.estadisticas.porcentaje_tiros_libres}%")
            print(f"Porcentaje tiros triples: {jugador.estadisticas.porcentaje_tiros_triples}%")
        else:
            print("Índice de jugador no válido.")

    def export_player_stats_to_csv(self, index, csv_filename):
        if 0 <= index < len(self.jugadores):
            jugador = self.jugadores[index]
            with open(csv_filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["nombre", "posicion", "temporadas", "puntos_totales", "promedio_puntos_por_partido",
                                 "rebotes_totales", "promedio_rebotes_por_partido", "asistencias_totales",
                                 "promedio_asistencias_por_partido", "robos_totales", "bloqueos_totales",
                                 "porcentaje_tiros_de_campo", "porcentaje_tiros_libres", "porcentaje_tiros_triples"])
                writer.writerow([jugador.nombre, jugador.posicion, jugador.estadisticas.temporadas,
                                 jugador.estadisticas.puntos_totales, jugador.estadisticas.promedio_puntos_por_partido,
                                 jugador.estadisticas.rebotes_totales, jugador.estadisticas.promedio_rebotes_por_partido,
                                 jugador.estadisticas.asistencias_totales, jugador.estadisticas.promedio_asistencias_por_partido,
                                 jugador.estadisticas.robos_totales, jugador.estadisticas.bloqueos_totales,
                                 jugador.estadisticas.porcentaje_tiros_de_campo, jugador.estadisticas.porcentaje_tiros_libres,
                                 jugador.estadisticas.porcentaje_tiros_triples])
            print(f"Las estadísticas de {jugador.nombre} se han exportado a {csv_filename}.")
        else:
            print("Índice de jugador no válido.")

    def search_player_by_name(self, player_name):
        for jugador in self.jugadores:
            if re.search(player_name, jugador.nombre, re.IGNORECASE):
                print(f"Logros de {jugador.nombre}:")
                for logro in jugador.logros:
                    print(logro)

    def average_points_per_game(self):
        total_points = 0
        total_seasons = 0
        for jugador in self.jugadores:
            total_points += jugador.estadisticas.puntos_totales
            total_seasons += jugador.estadisticas.temporadas
        if total_seasons > 0:
            average_ppg = total_points / total_seasons
            print(f"Promedio de puntos por partido de todo el equipo: {average_ppg:.2f}")
        else:
            print("No hay datos de temporadas para calcular el promedio.")

    def is_hall_of_fame_member(self, player_name):
        for jugador in self.jugadores:
            if re.search(player_name, jugador.nombre, re.IGNORECASE):
                if "Salón de la Fama" in jugador.logros:
                    print(f"{jugador.nombre} es miembro del Salón de la Fama del Baloncesto.")
                    return
        print(f"{player_name} no es miembro del Salón de la Fama del Baloncesto.")

    def player_with_most_rebounds(self):
        most_rebounds = 0
        best_rebounder = None
        for jugador in self.jugadores:
            if jugador.estadisticas.rebotes_totales > most_rebounds:
                most_rebounds = jugador.estadisticas.rebotes_totales
                best_rebounder = jugador.nombre
        if best_rebounder:
            print(f"Jugador con la mayor cantidad de rebotes totales: {best_rebounder} ({most_rebounds} rebotes)")
        else:
            print("No se encontraron datos de rebotes.")