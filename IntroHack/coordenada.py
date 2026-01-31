from geopy.geocoders import Nominatim

def obtener_direccion(lat, lon):
    geolocator = Nominatim(user_agent="direccion_app")
    location = geolocator.reverse((lat, lon), language="es")
    if location:
        return location.address, location.raw
    else:
        return None, None

if __name__ == "__main__":
    lat = -12.0486537
    lon = -77.0024975

    direccion, data = obtener_direccion(lat, lon)

    if direccion:
        print("📍 Dirección aproximada:")
        print(direccion)

        print("\n🔍 Datos desglosados:")
        address = data.get("address", {})
        for clave, valor in address.items():
            print(f"{clave}: {valor}")
    else:
        print("❌ No se pudo obtener la dirección.")
