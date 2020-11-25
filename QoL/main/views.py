from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import JsonResponse

# @login_required(redirect_field_name='next', login_url='')
from django.contrib import auth
import json
def login(request):
    print(12)
    # here you get the post request username and password
    username = request.GET.get('username', '')
    print(12)
    password = request.GET.get('password', '')

    # authentication of the user, to check if it's active or None
    user = auth.authenticate(username=username, password=password)
    print(password)

    if user is not None:
        print(14)
        
        if user.is_active:
            # this is where the user login actually happens, before this the user
            # is not logged in.
            auth.login(request, user)
            print(15)

            
            return JsonResponse({"status":"400"})

    else :
        return HttpResponseRedirect("Invalid username or password")
# Create your views here.
# @login_required
# def home(request):
#     return render(request, 'polls/detail.html', {'poll': p})