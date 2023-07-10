import requests

from config_drf import settings


def get_cat(request):
    url1 = 'http://127.0.0.1:8000/drf/api/v1/dish/categories/'
    response1 = requests.get(url1)
    cats = response1.json()
    return {'cats': cats}
