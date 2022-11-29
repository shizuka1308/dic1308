from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from common import file_storage_utility
from severity import admin

import traceback


# Create your views here.

class PredictionDetails(APIView):
    @staticmethod
    def post(request):
        try:
            temperature = request.data['temperature']
            humidity = request.data['humidity']
            pressure = request.data['pressure']
            visibility = request.data['visibility']
            wind_speed = request.data['wind_speed']
            precipitation = request.data['precipitation']
            if isinstance(temperature, int):
                temperature = temperature
            if isinstance(humidity, int):
                humidity = humidity
            if isinstance(pressure, int):
                pressure = pressure
            if isinstance(visibility, int):
                visibility = visibility
            if isinstance(wind_speed, int):
                wind_speed = wind_speed
            if isinstance(precipitation, int):
                precipitation = precipitation
            results = [temperature,humidity,pressure,visibility,wind_speed, precipitation]
            return Response({'result': results}, status=200)
        except Exception as e:
            traceback.format_exc()
            return Response({"message": "Exception Error " + str(e)})
