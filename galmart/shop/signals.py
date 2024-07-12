import requests
from retry import retry

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Order

@retry(tries=5, delay=1)
def get_token(credentials):
    url = 'http://127.0.0.1:8000/api/login/'
    data = {
        'username':credentials['username'],
        'password':credentials['password']
    }
    response = requests.post(url, data = data)
    if response.status_code != 200:
        print(f"Retrying to authorize due to {response.status_code}")
        raise Exception(f"Failed to authorize: {response.status_code}")
    token = response.json()['key']
    print("TOKEN",token)
    return token

@retry(tries=5, delay=1)
def send_data(token, order):
    url = "http://127.0.0.1:8000/api/order/"
    params = {
        'Authorization':f'token {token}'
    }
    data = {
        'order_id':order.id,
        'order_amount':order.amount,
        'shop':order.shop.id
    }
    response = requests.post(url, params = params, data = data)
    if response.status_code != 201:
        print(f"Retrying to send order data due to {response.status_code}")
        raise Exception(f"Failed to send data: {response.status_code}")
    return response

@receiver(post_save, sender=Order)
def order(sender, instance, created, **kwargs):
    if instance.status == instance.Status.FINISHED:
        credentials = {
            'username':'admin',
            'password':'123'
        }
        token = get_token(credentials)
        try:
            send_data(token, instance)
        except Exception as e:
            print(f"Signal was not able so send order data due to {e}")

        