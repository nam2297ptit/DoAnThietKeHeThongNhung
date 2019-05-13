from django.shortcuts import render
from django.utils import timezone
from .models import Sensor
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def sensor(request):
	Id = Sensor.objects.order_by('-id')[:5]
	Time = Sensor.objects.latest('Date_and_Time')
	Temperature = Sensor.objects.values_list('Temperature',flat=True).order_by('-id')[:5]
	Humidity = Sensor.objects.values_list('Humidity',flat=True).order_by('-id')[:5]


	char1= Sensor.objects.values_list('Temperature',flat=True).order_by('-id')[:10]
	char2= Sensor.objects.values_list('Humidity',flat=True).order_by('-id')[:10]
	Time_char= Sensor.objects.values_list('Date_and_Time',flat=True).order_by('-id')[:10]
	tr = Sensor.objects.values_list('SensorID',flat=True).distinct()
	return render(request, 'sensor/sensor.html', {'Id':Id,'Time':Time,'Temperature':Temperature,'Humidity':Humidity,'char1':char1,'char2':char2,'Time_char':Time_char,'tr':tr})
@login_required
def get_more_tables(request):
    order =  Sensor.objects.order_by('-id')[:5]
    return render(request, 'sensor/get_more_tables.html', {'order': order})
@login_required
def get_more_values(request):
    values =  Sensor.objects.latest('Date_and_Time')
    return render(request, 'sensor/get_more_values.html', {'values': values})