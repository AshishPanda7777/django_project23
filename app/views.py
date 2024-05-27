from django.shortcuts import render

# Create your views here.
from django.http  import HttpResponse
from app.models import *
from app.forms import  *
def insert_topic(request):
    ETFO=Topicpage()
    d={'ETFO':ETFO}
    

    if request.method == 'POST':
        TFDO = Topicpage(request.POST)
        if TFDO.is_valid():
            tn = TFDO.cleaned_data['tn']
            TO = TOPIC.objects.get_or_create(topic_name=tn)[0]
            return HttpResponse('Data inserted ')
        else:
            return HttpResponse('Invalid data')
    return render(request, 'insert_topic.html', d)


def insert_webpage(request):
    EWFO=webpage()
    d={'EWFO':EWFO}
    
    if request.method=='POST':
        WFDO=webpage(request.POST)
        if WFDO.is_valid():
            tn=WFDO.cleaned_data['tn']
            na=WFDO.cleaned_data['na']
            ur=WFDO.cleaned_data['ur']
            em=WFDO.cleaned_data['em']
            RTO=TOPIC.objects.get(topic_name=tn)
            WO=WEBPAGE.objects.get_or_create(topic_name=RTO,name=na,url=ur,email=em)[0]
            WO.save()
            return HttpResponse('Webpage is inserted succesfully')
        else:
            return HttpResponse('Invalid data')
    return render(request,'insert_webpage.html',d)


def insert_accessrecord(request):
    EAFO=accessrecord()
    d={'EAFO':EAFO}
    
    if request.method=='POST':
        AFDO=accessrecord(request.POST)
        if AFDO.is_valid():
            na=AFDO.cleaned_data['na']
            da=AFDO.cleaned_data['da']
            au=AFDO.cleaned_data['au']
            RWO=WEBPAGE.objects.get(name=na)
            AO=ACCESS_RECORD.objects.get_or_create(name=RWO,date=da,author=au)[0]
            AO.save()
            return HttpResponse('Access record inserted succesfully')
        else:
            return HttpResponse('invalid data')
    return render(request,'insert_accessrecord.html',d)