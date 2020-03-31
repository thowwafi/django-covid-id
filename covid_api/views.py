from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def index(request):
    req = requests.get("https://indonesia-covid-19-api.now.sh/api/provinsi")
    print(req.status_code)
    data = req.json()
    data = data.get('data')

    context = {
        'data': data
        }
    return render(request, 'index.html', context)