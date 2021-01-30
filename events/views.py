from django.shortcuts import render

# Create your views here.

def ourevents(request):
    return render(request,'events/events.html',{})
    