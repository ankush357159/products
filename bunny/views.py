from urllib import response
from django.http import HttpResponse
from django.shortcuts import redirect, render
from bunny.forms import MyPetForm

from django.contrib.sessions.models import Session
from django.utils.encoding import force_str
import base64
import pickle

def home(request):
    return render(request, 'bunny/index.html')


def myPetCreateView(request):

    if request.method == 'POST':
        form = MyPetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/')
    

    else:
        form = MyPetForm()
        

    return render(request, 'bunny/my-pet.html', {'form': form})

def setCookie(request):
    response = HttpResponse("Cookie set")

    if request.COOKIES.get('my_cookie'):
        message = "Thanks for visiting again"
        val = int(request.COOKIES.get('my_cookie')) 
    else:
        message = "You are visiting for the first time"
        val = 1

    # response.set_cookie("my_cookie", val)
    response.set_cookie("my_cookie", message, 3600*24) #setting cookie for a day
    response.set_cookie("visits", val)

    return response


def getCookie(request):
    cookie_msg = request.COOKIES.get('my_cookie')
    cookie_val = request.COOKIES.get('visits')    

    return HttpResponse("This is cookie response: {0} and {1}".format(cookie_msg, cookie_val))


def test_session(request):
    request.session.set_test_cookie()
    return HttpResponse("Testing session cookie")

def test_delete(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        response = HttpResponse("Cookie Test Passed")
    else:
        response = HttpResponse("Cookie test Failed")

    return response


def save_session_data(request):
    request.session['id'] = 1
    request.session['name'] = 'root'
    request.session['password'] = 'rootpassword'
    return HttpResponse("Session Data Saved")


def access_saved_data(request):
    response = ""
    if request.session.get('id'):
        response += "Id: {0} <br>".format(request.session.get('id'))
    if request.session.get('name'):
        response += "Name : {0} <br>".format(request.session.get('name'))
    if request.session.get('password'):
        response += "Password : {0} <br>".format(request.session.get('password'))
    if not response:
        return HttpResponse("No session data")
    else:
        return HttpResponse(response)

def delete_session_data(request):
    try:
        del request.session['id']
        del request.session['name']
        del request.session['password']
    except KeyError:
        pass
    return HttpResponse("Session data cleared")


def decode_session_data(request):
    s = Session.objects.get(pk='f3fi1p8swx2m14uclq1unbqm2v1cvw17')
    date = s.expire_date
    session_data = s.session_data
    data = s.get_decoded() 
    return HttpResponse("Values are {0} and {1} and {2}".format(session_data, data,date))




