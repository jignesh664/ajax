from django.db import reset_queries
from django.http.response import JsonResponse
from django.shortcuts import render,redirect
from .models import User

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt

# Create your views here.
def index(request):
    emp=User.objects.all()
    params={'emp':emp}
    return render(request,'index.html',params)

@csrf_exempt 
#insert data
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

#delete data
@csrf_exempt 
def delete_data(request):
    if request.method=="POST":
        id=request.POST.get('sid')
        print(id)
        pi=User.objects.get(pk=id)
        pi.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})

       

@csrf_exempt 
def edit(request,user_id = None):
    if request.method=="POST":
        s=User.objects.get(id=request.POST['user_id'])
        s.name=request.POST['name']
        s.email=request.POST['email']
        s.password=request.POST['password']
        s.save()
        return redirect('/')
    else:
        s=User.objects.get(id=user_id)
        params = {'user': s}
        return render(request,'edit.html', params) 