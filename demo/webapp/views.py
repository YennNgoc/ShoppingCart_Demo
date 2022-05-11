from multiprocessing import context
from django.shortcuts import render

# Create your views here.
import json
from django.conf import settings
import redis
from utils import get_db_handle
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

# Connect to our Redis instance
redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                  port=settings.REDIS_PORT, db=0)

@api_view(['GET', 'POST'])
def manage_items(request, *args, **kwargs):
    if request.method == 'GET':
        items = {}
        count = 0
        for key in redis_instance.keys("*"):
            items[key.decode("utf-8")] = redis_instance.get(key)
            count += 1
        response = {
            'count': count,
            'msg': f"Found {count} items.",
            'items': items
        }
        return Response(response, status=200)
    
    elif request.method == 'POST':
        item = json.loads(request.body)
        key = list(item.keys())[0]
        value = item[key]
        redis_instance.set(key, value)
        response = {
            'msg': f"{key} successfully set to {value}"
        }
        return Response(response, 201)

#########################################
@api_view(['GET', 'PUT', 'DELETE'])
def manage_item(request, *args, **kwargs):
    if request.method == 'GET':
        if kwargs['key']:
            value = redis_instance.get(kwargs['key'])
            if value:
                response = {
                    'key': kwargs['key'],
                    'value': value,
                    'msg': 'success'
                }
                return Response(response, status=200)
            else:
                response = {
                    'key': kwargs['key'],
                    'value': None,
                    'msg': 'Not found'
                }
                return Response(response, status=404)
    elif request.method == 'PUT':
        if kwargs['key']:
            request_data = json.loads(request.body)
            new_value = request_data['new_value']
            value = redis_instance.get(kwargs['key'])
            if value:
                redis_instance.set(kwargs['key'], new_value)
                response = {
                    'key': kwargs['key'],
                    'value': value,
                    'msg': f"Successfully updated {kwargs['key']}"
                }
                return Response(response, status=200)
            else:
                response = {
                    'key': kwargs['key'],
                    'value': None,
                    'msg': 'Not found'
                }
                return Response(response, status=404)

    elif request.method == 'DELETE':
        if kwargs['key']:
            result = redis_instance.delete(kwargs['key'])
            if result == 1:
                response = {
                    'msg': f"{kwargs['key']} successfully deleted"
                }
                return Response(response, status=404)
            else:
                response = {
                    'key': kwargs['key'],
                    'value': None,
                    'msg': 'Not found'
                }
                return Response(response, status=404)

def hello_world(request, *args, **kwargs):
    if request.method == 'GET':
        items = {}
        count = 0
        for key in redis_instance.keys("*"):
            items[key.decode("utf-8")] = redis_instance.get(key).decode("utf-8")
            count += 1
        context = {
            'count': count,
            'msg': f"Found {count} items.",
            'items': items
        }
    return render(request, 'hello_world.html', context)

def cart(request, *args, **kwargs):
    if request.method == 'GET':
        items = {}
        count = 0
        for key in redis_instance.keys("*"):
            items[key.decode("utf-8")] = redis_instance.get(key).decode("utf-8")
            count += 1
        context = {
            'count': count,
            'msg': f"Found {count} items.",
            'items': items
        }
    return render(request, 'shoppingcart.html', context)

def product(request):
    db_handle, _ = get_db_handle('mongodb', 'localhost', '27017','','')
    product = db_handle["product"]
    cursor = product.find({})
    tmp = []
    for document in cursor:
        tmp.append(document)
    test = {
        "product":tmp
    }
    return render(request, 'catalog.html', context={"product":tmp})

def detail(request,*args, **kwargs):
    db_handle, _ = get_db_handle('mongodb', 'localhost', '27017','','')
    product = db_handle["product"]
    tmp = product.find({ "product_id" : kwargs['product_id'] })
    test = {
        "product":tmp
    }
    return render(request, 'catalog.html', context={"product":tmp})

def add_pd(request):
    current_user = request.user.id
    context = {
        "user":current_user
    }
    return render(request, 'page.html', context)
