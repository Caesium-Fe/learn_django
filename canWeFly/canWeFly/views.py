from django.http import HttpResponse
from django_redis import get_redis_connection


def index(request):
    return HttpResponse("alkjdslkjaskld")


def login(request):
    print('asd')
    conn = get_redis_connection('default')
    conn.set('xx3', 'oo3')
    s = conn.get('xx3')
    return HttpResponse(s)
