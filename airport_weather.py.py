import urllib.request
import json

print("✈️ Airport Weather Checker")

airports = {
    "1": {"name": "Ankara Esenboga Airport", "lat": 40.1281, "lon": 32.9951},
    "2": {"name": "Istanbul Airport", "lat": 41.2753, "lon": 28.7519},
    "3": {"name": "Seoul Incheon Airport", "lat": 37.4602, "lon": 126.4407},
    "4": {"name": "Milan Malpensa Airport", "lat": 45.6306, "lon": 8.7281}
}

print("""
Choose Airport:
1 - Ankara Esenboga
2 - Istanbul Airport
3 - Seoul Incheon
4 - Milan Malpensa
""")

choice = input("Enter airport number: ")

if choice in airports:
    airport = airports[choice]
    url = f"https://api.open-meteo.com/v1/forecast?latitude={airport['lat']}&longitude={airport['lon']}&current_weather=true"

    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    weather = data["current_weather"]

    print("\n----- AIRPORT WEATHER REPORT -----")
    print(f"Airport: {airport['name']}")
    print(f"Temperature: {weather['temperature']} °C")
    print(f"Wind Speed: {weather['windspeed']} km/h")
    print(f"Wind Direction: {weather['winddirection']}°")

    if weather["windspeed"] > 35:
        print("Flight Condition: RISKY ⚠️")
    else:
        print("Flight Condition: NORMAL ✅")
else:
    print("Invalid airport selection.")