from django.shortcuts import render, redirect
from models import *
from django.db import connection, transaction

cursor = connection.cursor()


# Create your views here.
def index(request):
    context={
        "users":User.objects.all()
        }
    return render(request,'index.html',context)
def create(request):
   
    User.objects.create(fullname=request.POST['fullname'],email=request.POST['email'])
   

    return redirect('/')
def edit(request, id):
    context={
        "users":User.objects.get(id=id),
    }
    return render(request,'edit.html', context)
def delete(request, id):
    bill = User.objects.get(id=id)
    bill.delete()
    return redirect('/')
def change(request, id):
    errors = User.objects.validate(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            error(request, message, extra_tags=field)
        
        return redirect('/users/?p=%s' % id)



    user_to_update = User.objects.get(id=id)
    user_to_update.fullname = request.POST['fullname']
    user_to_update.email = request.POST['email']
    user_to_update.save()
    return redirect('/')
def new(request):
    return render(request,"create.html")
def show(request, id):
    context={
        "users":User.objects.get(id=id)
        }
    return render(request,"show.html",context)
