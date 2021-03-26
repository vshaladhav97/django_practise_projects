from django.shortcuts import render
from django.http import HttpResponse


def setsession(request):
    request.session['sname'] = 'vishal'
    request.session['semail'] = 'vshaladhav@gmail.com'
    return HttpResponse("session is set")


def getsession(request):
    studentname = request.session['sname']
    studentemail = request.session['semail']
    return HttpResponse(studentname+" "+studentemail)


def cookie_session(request):
    request.session.set_test_cookie()
    return HttpResponse("<h1>dataflair</h1>")
def cookie_delete(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        response = HttpResponse("dataflair<br> cookie createed")
    else:
        response = HttpResponse("Dataflair <br> Your browser doesnot accept cookies")
    return response
