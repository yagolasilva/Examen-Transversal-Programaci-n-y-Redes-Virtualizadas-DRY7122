from geopy.geocoders import Nominatim
from geopy.distance import geodesic

def obtener_coordenadas(ciudad):
    geolocator = Nominatim(user_agent="mi_app")
    location = geolocator.geocode(ciudad)
    if location:
        return (location.latitude, location.longitude)
    else:
        return None

def calcular_distancia(origen, destino):
    coords_origen = obtener_coordenadas(origen)
    coords_destino = obtener_coordenadas(destino)
    if not coords_origen or not coords_destino:
        raise ValueError("No se pudo obtener las coordenadas para las ciudades proporcionadas.")
    distancia = geodesic(coords_origen, coords_destino)
    return distancia

def mostrar_informacion_viaje(origen, destino, distancia, medio_transporte):
    distancia_km = distancia.kilometers
    distancia_millas = distancia.miles
    duracion_horas = distancia.kilometers / 60  # Suponiendo una velocidad promedio de 60 km/h
    duracion_minutos = duracion_horas * 60
    
    print(f"\nInformación del Viaje:")
    print(f"Distancia en kilómetros: {distancia_km:.2f} km")
    print(f"Distancia en millas: {distancia_millas:.2f} mi")
    print(f"Duración aproximada del viaje en horas: {duracion_horas:.2f} horas")
    print(f"Duración aproximada del viaje en minutos: {duracion_minutos:.2f} minutos")
    
    narrativa = f"Viajando desde {origen} hasta {destino} en {medio_transporte}, la distancia es de {distancia_km:.2f} kilómetros y la duración aproximada del viaje es de {duracion_horas:.2f} horas."
    print("\nNarrativa del Viaje:")
    print(narrativa)

def main():
    while True:
        origen = input("Ciudad de Origen: ")
        if origen.lower() == 's':
            break
        destino = input("Ciudad de Destino: ")
        if destino.lower() == 's':
            break
        
        medio_transporte = input("Seleccione el medio de transporte (1. Conducir, 2. Caminar, 3. Bicicleta): ")
        if medio_transporte == '1':
            medio_transporte = "Conduciendo"
        elif medio_transporte == '2':
            medio_transporte = "Caminando"
        elif medio_transporte == '3':
            medio_transporte = "En Bicicleta"
        else:
            print("Opción de medio de transporte no válida. Se asumirá Conduciendo.")
            medio_transporte = "Conduciendo"

        try:
            distancia = calcular_distancia(origen, destino)
            mostrar_informacion_viaje(origen, destino, distancia, medio_transporte)
        except ValueError as e:
            print(e)

        salir = input("\n¿Desea salir? (s para salir): ")
        if salir.lower() == 's':
            break

if __name__ == "__main__":
    main()
