import tkinter as tk
import requests


def know():
    town = city.get()
    url_geo = f"https://geocoding-api.open-meteo.com/v1/search?name={town}&language=ru"
    geo_data = requests.get(url_geo).json()

    if not geo_data.get("results"):
        result.config(text="Город не найден")
        return

    lat = geo_data["results"][0]["latitude"]
    lon = geo_data["results"][0]["longitude"]

    url_weather = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m"
    weather_data = requests.get(url_weather).json()

    temp = weather_data["current"]["temperature_2m"]
    humidity = weather_data["current"]["relative_humidity_2m"]

    result.config(text=f"{town}: {temp}°C, влажность {humidity}%")

root = tk.Tk()
root.title("Погода")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

main = tk.Label(root, text="Прогноз погоды", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#1a3c5e")
main.pack(pady=15)

enter_city = tk.Label(root, text="Введите город", font=("Arial", 11, "bold"), bg="#f0f0f0", fg="#666666")
enter_city.pack(pady=10)

city = tk.Entry(root, font=("Arial", 12), width=20)
city.pack(pady=10)

weather = tk.Button(root, text="узнать погоду", command=know, bg="#3498db", fg="white", font=("Arial", 11, "bold"), width=15)
weather.pack(pady=10)

result = tk.Label(root, text="", font=("Arial", 12, "bold"), fg="#1a3c5e")
result.pack(pady=15)

root.mainloop()