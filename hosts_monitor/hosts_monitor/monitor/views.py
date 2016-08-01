from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Node
from .forms import Drop_name_choice, NodeForm, LogInForm
from django.contrib.auth.decorators import login_required

def index(request):

    nodes = Node.objects.all()
    form = Drop_name_choice()
    edit = NodeForm()
    user = User.objects.all()
    loginForm = LogInForm()

    if request.GET:
        if 'id' in request.GET:
            id = request.GET['submit']
    
    if request.POST: #ping

        if 'node_to_ping' in request.POST:
            id = request.POST['node_to_ping']
            node = Node.objects.get(pk=id)
            node.ping('hostname')

        elif 'node_to_delete' in request.POST: #node delete

            id_delete = request.POST['node_to_delete']
            instance = Node.objects.get(pk=id_delete)
            instance.delete()

        elif 'drop_state_choice' in request.POST: #dropdown list
            name = request.POST['drop_state_choice']
            for node in Node.objects.all():
                node.ping(name)

    if request.POST and request.is_ajax():
        edit = NodeForm(request.POST)
        if 'hostname' and 'ip' in request.POST:
            if edit.is_valid():
                edit.cleaned_data['hostname']
                edit.cleaned_data['ip']
                edit.save()
                return HttpResponse('host_saved')
            else:
                return render(request, 'monitor/node_form.html', {'nodes':nodes, 'form':form,'edit':edit})

        elif 'username' and 'password' in request.POST:
            loginForm = LogInForm(request.POST or None)
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                return HttpResponse('send_back')
            else:
                return render(request, 'monitor/editor.html', {'loginForm': loginForm})

        elif 'logout' in request.POST:
            logout(request)
            return HttpResponse('logout')
        else:
            return render(request,'monitor/index.html',{'nodes':nodes, 'form':form, 'edit':edit, 'loginForm': loginForm})

    return render(request,'monitor/index.html',{'nodes':nodes, 'form':form, 'edit':edit, 'loginForm': loginForm})





