from django.shortcuts import render,redirect
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from models import TodoList
from django.http import HttpResponse
from django.core import serializers
import json
from datetime import datetime

# Create your views here.

def todolist(request):
    todolist = TodoList.objects.all()
    paginator = Paginator(todolist, 3)
    page = request.GET.get('page')
    try:
        tl = paginator.page(page)
    except PageNotAnInteger:
        tl = paginator.page(1)
    except EmptyPage:
        tl = paginator.page(paginator.num_pages)
    return render(request,'todolist.html',locals())

def dosearch(request):
    try:
        item = request.GET.get("searchitem")
    except:
        pass
    if(item):
        todolist = TodoList.objects.filter(item__contains=item)
    else:
        todolist = TodoList.objects.all()
    paginator = Paginator(todolist,3)
    page = request.GET.get('page')
    try:
        tl = paginator.page(page)
    except PageNotAnInteger:
        tl = paginator.page(1)
    except EmptyPage:
        tl = paginator.page(paginator.num_pages)

    return render(request, 'todolist.html', locals())

def additem(request):

    try:
        item = request.GET.get('item')
        newitem = TodoList(item=item,intime=datetime.now())
        newitem.save()
    except Exception as e:
        raise e

    return redirect(request.META['HTTP_REFERER'])

def saveedit(request):

    try:
        edititem = request.GET.get('edititem')
        id = request.GET.get('id')
        updateitem = TodoList.objects.get(id=id)
        updateitem.item=edititem
        updateitem.intime=datetime.now()
        updateitem.save()
    except Exception as e:
        raise e

    return redirect(request.META['HTTP_REFERER'])

def delete_ajax(request):

    try:
        item = request.GET.get('item')
        delteitem = TodoList.objects.get(item=item)
        delteitem.deletetag=1
        delteitem.save()
    except Exception as e:
        raise e

    return HttpResponse(json.dumps({"result":1}), content_type="application/json")