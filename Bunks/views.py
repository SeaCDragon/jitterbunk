from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Bunk
from django.template import loader
from django.urls import reverse
from django.utils import timezone

# Create your views here.
def index(request):
    bunks = Bunk.objects.order_by("-time")
    template = loader.get_template('Bunks/index.html')
    context = {
        "list_of_bunks": bunks
    }
    return HttpResponse(template.render(context, request))

def user(request, from_user):
    sent_bunks = Bunk.objects.filter(from_user = from_user)
    received_bunks = Bunk.objects.filter(to_user = from_user)
    template = loader.get_template('Bunks/user.html')
    user = User.objects.get(pk=from_user)
    context = {
        "user": user,
        "sent": sent_bunks,
        "received": received_bunks,
    }
    return HttpResponse(template.render(context, request))

def new(request):
    
    if request.method == 'POST':
        sender = User.objects.get(pk=request.POST['sender'])
        receiver = User.objects.get(pk=request.POST['receiver'])
        bunk = Bunk()
        bunk.from_user = sender
        bunk.to_user = receiver
        bunk.time = timezone.now()
        bunk.save()
        return HttpResponseRedirect(reverse('Bunks:index'))
    else:
        template = loader.get_template('Bunks/new.html')
        context = {
            "users": User.objects.all()
        }
        return HttpResponse(template.render(context, request))