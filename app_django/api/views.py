import datetime
import os

import redis
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .integrations.google_weather import get_temperature, UncorrectCity

# Connect to our Redis instance
redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                   port=settings.REDIS_PORT, db=0)


@api_view(['GET'])
def weather(request, *args, **kwargs):
    if request.method == 'GET':
        if kwargs and 'key' in kwargs:
            city = kwargs['key']
        else:
            city = os.environ.get('CITY')
        value = redis_instance.get(city)
        if value:
            updated_time = redis_instance.get('updated_time')
            response = {
                'city': city,
                'value': value,
                'updated_at': updated_time
            }
            return Response(response, status=200)
        else:
            try:
                value, _, _, _ = get_temperature(city)
                redis_instance.set(city, value, ex=60)
                updated_time = datetime.datetime.utcnow()
                time_string = updated_time.ctime()
                redis_instance.set('updated_time', time_string, ex=60)
                response = {
                    'city': city,
                    'value': value,
                    'updated_at': time_string
                }
                return Response(response, status=200)
            except UncorrectCity as e:
                response = {
                    'msg': 'Invalid request',
                }
                return Response(response, status=400)
