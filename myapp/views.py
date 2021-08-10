from django.db import reset_queries
from django.http.response import JsonResponse
from django.shortcuts import render
from .models import User

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt

# Create your views here.
def index(request):
    emp=User.objects.all()
    params={'emp':emp}
    return render(request,'index.html',params)

@csrf_exempt 

def save_data(request):
    if request.method=="POST":
        s=User()
        s.name=request.POST['name']
        s.email=request.POST['email']
        s.password=request.POST['password']
        s.save()
        users=User.objects.values()
        user_data=list(users)
        return JsonResponse({'status':'save','user_data':user_data})  
    else:
       return JsonResponse({'status':0})


