# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from ..loginapp.models import *
from .models import *
from django.contrib import messages

# Create your views here.

def index(request):
    user = Users.objects.filter(id = request.session['User_id'])
    items = Wish.objects.all 
    context = {
        'stuff': items,
        'person': user[0],
        'my_stuff': Wish.objects.filter(creator=request.session['User_id'])|Wish.objects.filter(join=Users.objects.get(id=request.session['User_id']))
    }
    return render(request,"examapp/index.html", context)

def new(request):
    return render(request,'examapp/new.html')

def create(request):
    print "Entered Create"
    errors = Wish.objects.polish(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request,error)
        return redirect('/exam/new')
    else:
        users = Users.objects.filter(id = request.session['User_id'])

        Wish.objects.create(
            name = request.POST['name'],
            creator = users[0]
        )
        return redirect('/exam')

def show(request,id):
    items = Wish.objects.get(id=id)
    context={
        "things":items

    }
    return render(request,'examapp/show.html',context)

def added(request,id):
    users = Users.objects.get(id = request.session['User_id'])
    things = Wish.objects.get(id=id)
    things.join.add(users)
    things.save()
    return redirect('/exam')

def remove(request,id):
    users = Users.objects.get(id = request.session['User_id'])
    things = Wish.objects.get(id=id)
    things.join.remove(users)
    things.save()
    return redirect('/exam')

def delete(request,id):
    users= Users.objects.filter(id = request.session['User_id'])
    things = Wish.objects.get(id=id)
    if users[0].id == things.creator.id:
        things.delete()
        return redirect('/exam')
    else:
        messages.error(request,"If you don't make it.... You can't delete it!")
        return redirect('/exam')

def logout(request):
    request.session.clear()
    return redirect('/')