import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response

API_KEY = "YOUR_API_KEY"

@api_view(['GET'])
def weather_api(request):
    city = request.GET.get('city')

    if not city:
        return Response({"error": "City parameter is required"})

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        return Response({"error": "City not found"})

    weather_data = {
        "city": city,
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"]
    }

    return Response(weather_data)