from django.shortcuts import render

# Create your views here.
from app.models import *

# Create your views here.
def display_tables(request):

    TOO=Topic.objects.all()
    d={'topics':TOO}
    return render(request,'display_tables.html',d)

def display_webpage(request):

    WEBPA=Webpage.objects.all()
    d={'wepa':WEBPA}
    return render(request,'display_webpage.html',d)


def display_access(request):
     ACCR=AccessRecord.objects.all()
     d={'access':ACCR}
     return render(request,'display_access.html',d)




def insert_topic(request):
    TOI=input('Enter the data :')
    TO=Topic.objects.get_or_create(topic_name=TOI)[0]
    TO.save()
    NTO=Topic.objects.all()
    d={'topics':NTO}
    return render(request,'display_tables.html',d)


def insert_webpage(request):
    WOI=input('Enter topic')
    NOI=input('Enter name')
    UOI=input('Enter URL')
    WPO=Topic.objects.get(topic_name=WOI)
    WO=Webpage.objects.get_or_create(topic_name=WPO,name=NOI,url=UOI)[0]
    WO.save()
    WWI=Webpage.objects.all()
    d={'wepa':WWI}
    return render(request,'display_webpage.html',d)



def insert_accessrecord(request):
    ACC=int(input('enter pk value:'))
    ACC1=input('enter date:')
    ACC2=input('enter Aouthor:')
    ACC0=Webpage.objects.get(pk=ACC)
    NAO=AccessRecord.objects.get_or_create(name=ACC0,date=ACC1,Author=ACC2)[0]
    NAO.save()
    NARO=AccessRecord.objects.all()
    d={'access':NARO}
    return render(request,'display_access.html',d)