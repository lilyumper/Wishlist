# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
import bcrypt
import re
from . models import Checker, Users
from django.contrib import messages


# Create your views here.


def index(request):
    return render(request, "index.html")


def login(request):
    errors = Users.objects.login_validator(request.POST)
    for error in errors:
        messages.error(request, error)
        return redirect('/')
    else:
        u = Users.objects.get(email=request.POST['lemail'])
        request.session['User_id'] = u.id
        return redirect('/exam')

            

def process(request):
    errors = Users.objects.basic_validator(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request,error)
        return redirect('/')
    else:
        hash1 = bcrypt.hashpw(request.POST['password'].encode(),bcrypt.gensalt())        
        Users.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            birthday = request.POST['birthday'],
            email = request.POST['email'],
            password = hash1
        )
        user =Users.objects.last().id
        request.session['User_id'] = user
        
        return redirect('/exam')

        
    

def success(request):
    user= Users.objects.get(id=request.session['User_id'])
    context={
        'name': user
    }
   
    return render(request,'success.html',context)
