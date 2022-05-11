from multiprocessing import context
from django.shortcuts import render, redirect

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
db_handle, _ = get_db_handle('mongodb', 'localhost', '27017','','')

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
            items[key] = redis_instance.get(key)
            count += 1
        context = {
            'count': count,
            'msg': f"Found {count} items.",
            'items': items
        }
    return render(request, 'hello_world.html', context)

def cart(request, *args, **kwargs):
    if request.method == 'GET':
        items = []
        count = 0
        key = "cart:{}".format(request.user.id)
        list_product = redis_instance.hgetall(key)
        order_subtotal = 0
        for field in list_product:
            field = field.decode("utf-8")
            quantity = redis_instance.hget(key, field).decode("utf-8")
            product = db_handle["product"]
            tmp = product.find_one({ "product_id" : field })
            product_name = tmp["product_name"]
            price = tmp["product_info"]["product_price"]
            if "promotion" in tmp.keys():
                discount = float(tmp["promotion"]["discount"].split("%")[0])/100
                price = float(price) - float(price)*discount
            order_subtotal+=float(price)*int(quantity)
            category = tmp["product_type"]["product_type_description"]
            tmp_item = {}
            tmp_item["product_name"] = product_name
            tmp_item["quantity"] = quantity
            tmp_item["price"] = "{0:,} VND".format(int(price))
            tmp_item["category"] = category
            items.append(tmp_item)
        ship = 10000
        tax = 0.05
        if (order_subtotal == 0):
            ship = 0
            tax = 0
        total = (order_subtotal + ship)*tax + (order_subtotal + ship) 
        context = {
            'count': count,
            'msg': f"Found {count} items.",
            'items': items,
            "order_subtotal": "{0:,} VND".format(int(order_subtotal)),
            "total": "{0:,} VND".format(int(total)),
            "tax": "{0:,} VND".format(int((order_subtotal + ship)*tax)),
            "ship": "{0:,} VND".format(ship)
        }
    return render(request, 'shoppingcart.html', context)

def product(request):
    product = db_handle["product"]
    cursor = product.find({})
    tmp = []
    for document in cursor:
        tmp.append(document)
    return render(request, 'catalog.html', context={"product":tmp})
    

def detail(request,*args, **kwargs):
    product = db_handle["product"]
    tmp = product.find({ "product_id" : kwargs['product_id'] })
    return render(request, 'catalog.html', context={"product":tmp})

def add_pd(request, *args, **kwargs):
    current_user = request.user.id
    key = "cart:{}".format(current_user)
    field = kwargs['product_id']
    value = redis_instance.hincrby(key, field, 1)
    return redirect('/webapp/pd/')

def confirm_cart(request, *args, **kwargs):
    current_user = request.user.id
    key = "cart:{}".format(current_user)
    value = redis_instance.delete(key)
    return redirect('/webapp/cart/')