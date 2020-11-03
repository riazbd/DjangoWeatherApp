from django.shortcuts import render

# Create your views here.


def home(request):
    import json
    import requests
    if request.method == 'POST':
        cityName = request.POST['cityName']
        apiRequest = requests.get(
            "https://api.weatherapi.com/v1/forecast.json?key=2e0e896408bc4fb0a6e202912201810&q=" + cityName + "&days=1")
        try:
            api = json.loads(apiRequest.content)
        except Exception as error:
            api = "Error......"

        return render(request, 'home.html', {'api': api})
    else:
        # apiRequest = requests.get(
        #     "https://api.weatherapi.com/v1/forecast.json?key=2e0e896408bc4fb0a6e202912201810&q=" + cityName + "&days=1")
        # try:
        #     api = json.loads(apiRequest.content)
        # except Exception as error:
        #     api = "Error......"

        return render(request, 'home.html', {})


def about(request):
    return render(request, 'about.html', {})
