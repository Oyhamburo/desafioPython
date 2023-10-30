from clases.equipo import Equipo

def main():
    equipo = Equipo("db/db.json")
    while True:
        print("\nMenú de opciones:")
        print("1. Mostrar lista de jugadores")
        print("2. Mostrar estadísticas de un jugador")
        print("3. Exportar estadísticas a CSV")
        print("4. Buscar jugador por nombre")
        print("5. Calcular promedio de puntos por partido del equipo")
        print("6. Comprobar si un jugador es miembro del Salón de la Fama")
        print("7. Encontrar jugador con más rebotes totales")
        print("8. Salir")
        choice = input("Seleccione una opción: ")

        if choice == '1':
            equipo.list_players()
        elif choice == '2':
            index = int(input("Ingrese el índice del jugador: "))
            equipo.get_player_stats(index)
        elif choice == '3':
            index = int(input("Ingrese el índice del jugador a exportar: "))
            csv_filename = input("Ingrese el nombre del archivo CSV de destino: ")
            equipo.export_player_stats_to_csv(index, csv_filename)
        elif choice == '4':
            player_name = input("Ingrese el nombre del jugador a buscar: ")
            equipo.search_player_by_name(player_name)
        elif choice == '5':
            equipo.average_points_per_game()
        elif choice == '6':
            player_name = input("Ingrese el nombre del jugador a comprobar: ")
            equipo.is_hall_of_fame_member(player_name)
        elif choice == '7':
            equipo.player_with_most_rebounds()
        elif choice == '8':
            break
        else:
            print("Opción no válida. Por favor, elija una opción válida.")

if __name__ == '__main__':
    main()
