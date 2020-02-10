from django.shortcuts import render
from basicApp.forms import Mform
from basicApp.models import Client
#from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')
def register(request):
    form = Mform()
    print(request.method)
    if request.method=='POST':
        form = Mform(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'basic_app/index.html')
        else:
            return render(request,'basic_app/register.html',context={'form':form})
    return render(request,'basic_app/register.html',context={'form':form})

def detail(request):
    data =  Client.objects.all()
    return render(request,'basic_app/detail.html',context={'data':data})
