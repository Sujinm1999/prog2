from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Wishes
from .forms import WishForms
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            request.session['username']=username
            return redirect('/home/')
        else:
            messages.info(request,'Invalid details')
            return redirect('/')
    else:
        return render(request,'login.html')

def register(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already exist")
                return redirect('/register/')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Mail ID already exist")
                return redirect('/register/')
            else:
                user=User.objects.create_user(username=username,email=email,first_name=first_name,password=password1)
                user.save()
                return redirect('/')
        else:
            messages.info(request, "Password missmatch")
            return redirect('/register/')
    else:
        return render(request,'register.html')

# def home(request):
#     return HttpResponse("haii guys")

class TaskListView(ListView):
    model=Wishes
    template_name = 'task_view.html'
    context_object_name = 'obj1'

class TaskDetailView(DetailView):
    model=Wishes
    template_name = 'detail.html'
    context_object_name = 'i'

class TaskUpdateView(UpdateView):
    model=Wishes
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('covdetail',kwargs={ 'pk':self.object.id })

class TaskDeleteView(DeleteView):
    model=Wishes
    template_name = 'delete.html'
    success_url = reverse_lazy('covtask')

def task_view(request):
    obj1=Wishes.objects.all()
    if request.method=="POST":
        place=request.POST.get('place')
        priority = request.POST.get('priority')
        experience=request.POST.get('experience')
        obj=Wishes(place=place,priority=priority,experience=experience)
        obj.save()
    return render(request,"task_view.html",{'obj1':obj1})

def delete(request,wishid):
    wish=Wishes.objects.get(id=wishid)
    if request.method=="POST":
        wish.delete()
        return redirect('/home/')
    return render(request,'delete.html',{'wish':wish})

def update(request,id):
    wish=Wishes.objects.get(id=id)
    form=WishForms(request.POST or None,instance=wish)
    if form.is_valid():
        form.save()
        return redirect('/home/')
    return render(request,"edit.html",{'wish':wish,'form':form})