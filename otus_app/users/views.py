from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Users_info
from django.core import serializers


def index(request):
    info_about_users = Users_info.objects.all()

    return render(request, "otus_app/index.html", dict(user_list=info_about_users, title='Сведения о пользователях'))


@require_http_methods(['POST'])
def add(request):

    UserName = request.POST['UserName']
    FirstName = request.POST['FirstName']
    LastName = request.POST['LastName']
    Email = request.POST['Email']
    Phone = request.POST['Phone']

    user = Users_info(
                      UserName=UserName,
                      FirstName=FirstName,
                      LastName=LastName,
                      Email=Email,
                      Phone=Phone
                      )
    user.save()
    return redirect('index')


def delete(request, ID):
    users = Users_info.objects.get(ID=ID)
    users.delete()
    return redirect('index')


def update(request, ID):
    users = Users_info.objects.get(ID=ID)
    return render(request,"otus_app/update.html",{'users': users})

def uprec(request, ID):
    UserName = request.POST['UserName']
    FirstName = request.POST['FirstName']
    LastName = request.POST['LastName']
    Email = request.POST['Email']
    Phone = request.POST['Phone']

    users = Users_info.objects.get(ID=ID)
    users.ID = ID
    users.UserName = UserName
    users.FirstName = FirstName
    users.LastName = LastName
    users.Email = Email
    users.Phone = Phone
    users.save()
    return redirect("index")

