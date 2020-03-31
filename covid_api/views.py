from django.shortcuts import render
from django.http import HttpResponse
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

# Create your views here.
def index(request):
    url = "https://indonesia-covid-19-api.now.sh/api/provinsi"
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    req = session.get(url)
    print(req.status_code)
    data = req.json()
    data = data.get('data')

    context = {
        'data': data
        }
    return render(request, 'index.html', context)