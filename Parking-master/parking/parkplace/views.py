import datetime
import pytz
import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import placeSerializer

utc=pytz.UTC

class Get_place_List(APIView):
    def get(self, request):
        place = Place.objects.all()
        serialized = placeSerializer(place, many=True)
        return Response(serialized.data)
@csrf_exempt
def getdata(request):
    if request.method =="POST":
        now = datetime.datetime.utcnow()+datetime.timedelta(hours=4)
        now=utc.localize(now)
        a = request.body.decode()
        data = json.loads(a)
        status = data['data']
        check = Place.objects.filter(device_name=data['deviceName']).last()
        print(data)
        check_brone = check.reserves_set.all()
        def get_brone_or_not():
            for i in check_brone:
                if i.start_date <= now <= i.end_date:
                    print(i.start_date,'<=',now,'<=',i.end_date)
                    return True
        def get_status():
            if status== 'MA==' and not get_brone_or_not():
                print('MA OLDU')
                # check.bronetime_start = None
                # check.bronetime_end = None
                return 'free'
            elif status == 'MQ==' and not get_brone_or_not():
                print('MQ OLDU')
                # check.bronetime_start = None
                # check.bronetime_end = None
                return 'full'
            else:
                return 'brone'
        if check:
            check.status = get_status()
            check.save()

    else:
        # print("ths get")
        new= request.body.decode()
        print(new)
    return HttpResponse('200')

def index(request):

    return render (request, 'index.html',{'list':list})

def brone(request,dev_name):
    place = Place.objects.filter(device_name=dev_name).last()
    if request.POST and request.is_ajax():
        default = request.POST.get('info')
        now = datetime.datetime.utcnow()+datetime.timedelta(hours=4)
        now = utc.localize(now)
        start = datetime.datetime.strptime(default[:15], "%d/%m/%Y %H:%M")
        start = utc.localize(start)
        end = datetime.datetime.strptime(default[18:], "%d/%m/%Y %H:%M")
        end = utc.localize(end)
        Reserves.objects.create(
            start_date=start,
            end_date=end,
            to_place = place,
        )
        place.bronetime_start =start
        place.bronetime_end = end
        print(default)
        print(start,' ',now,' ',end)
        if start <= now <=end:
            place.status = 'brone'
            place.save()

    return render (request, 'brone.html')

def full(request):
    return render (request, 'full.html')

