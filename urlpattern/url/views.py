from url.models import Post
from django.shortcuts import render
from django.http import HttpResponse
import uuid

# Create your views here.


def showdetails1(request):
    return render(request, 'enroll/show.html')


def urldetail(request, my_id1):
    detail = Post.objects.filter(id=my_id1)
    student = {'id': my_id1, 'name': detail,
                'ids': 'this is id number {}'.format(my_id1)}
    # if my_id1 == '2':
    #     student = {'id':my_id1, 'name': detail1}

    return render(request, 'enroll/show2.html', student)


def urlint(request, my_id2):
    if my_id2 == 1:
        student = {'id': my_id2, 'name': 'vishal'}
    if my_id2 == 2:
        student = {'id': my_id2, 'name': 'ritin'}
    if my_id2 == 3:
        student = {'id': my_id2, 'name': 'yash'}

    return render(request, 'enroll/show3.html', student)


def profile(request, username='Default User'):
    return HttpResponse('<h1>This is a profile page! The user is {}.</h1>'.format(username))


def article(request, article_value):
    
    return HttpResponse('<h1>The article name is {}.</h1>'.format(article_value))


def uids(request, uid):
    return HttpResponse('<h1>The article name is {}.</h1>'.format(uid))


def repath(request, number):
    return HttpResponse('<h1>Post detial view pages: {}</h1>'.format(number))

def urldetails(request, my_id3):
    # detail = Post.objects.filter(slug=my_id1)
    student = {'id': my_id3, 'ids': 'the string is {}'.format(my_id3)}
    # if my_id1 == '2':
    #     student = {'id':my_id1, 'name': detail1}

    return render(request, 'enroll/show4.html', student)