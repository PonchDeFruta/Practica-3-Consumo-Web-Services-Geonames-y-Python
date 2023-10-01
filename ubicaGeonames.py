import requests

def obtener_informacion_ubicacion(geonames_username, lugar):
    url = f"http://api.geonames.org/searchJSON?name={lugar}&maxRows=1&username={geonames_username}"

    try:
        response = requests.get(url)
        data = response.json()
        print(data)
        if "geonames" in data and data["geonames"]:
            ubicacion = data["geonames"][0]
            print(f"Nombre: {ubicacion['name']}")
            print(f"País: {ubicacion['countryName']}")
            print(f"Población: {ubicacion['population']}")
            print(f"Codigo de País: {ubicacion['countryId']}")
        else:
            print("Ubicación no encontrada.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    #Coloca tu usuario de geonames
    geonames_username = "pxnchfermon"

    lugar = "Mexico"  # Cambia esto a la ubicación que desees consultar
    obtener_informacion_ubicacion(geonames_username, lugar)
