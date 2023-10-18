import requests

def obtener_datos_meteorologicos(api_key, ciudad):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}"

    try:
        response = requests.get(url)
        data = response.json()
        print(data)
         
        if "main" in data and "weather" in data and "sys" in data:
           
            temperatura = data["main"]["temp"] - 273.15  # Convertir de Kelvin a Celsius
            condiciones_climaticas = data["weather"][0]["description"]
            country = data["sys"]["country"]
            city = data["name"]
            print(f"Temperatura: {temperatura:.2f}°C")
            print(f"Condiciones Climáticas: {condiciones_climaticas}")
            print (f"Ubicacion Especifica: {country}, {city}")

        else:
            print("Datos meteorológicos no disponibles.")
            print(response)
    except Exception as e:
        print(f"Error: {str(e)}")



if __name__ == "__main__":
    #tu_api_key_de_openweathermap
    api_key = "52478600bb1675e4cb1fd565206e8e90" #tu api key
    ciudad = "London"  # Cambia esto a la ciudad que desees consultar
    obtener_datos_meteorologicos(api_key, ciudad)
