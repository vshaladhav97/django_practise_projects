from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from .models import Post, Like
from django.http import HttpResponse
# from django.contrib.auth.forms import UserCreationForm
# from django.views.generic.edit import CreateView
# Create your views here.


# class SignUpView(CreateView):
#     template_name = 'misc/signup.html'
#     form_class = UserCreationForm


# def validate_username(request):
#     username = request.GET.get('username', None)
#     data = {
#         'is_taken': User.objects.filter(username__iexact=username).exists()
#     }
#     return JsonResponse(data)
def index(request):
    posts = Post.objects.all()  # Getting all the posts from database
    return render(request, 'enroll/index.html', {'posts': posts})


def likePost(request):
    if request.method == 'GET':
        post_id = request.GET['post_id']
        likedpost = Post.objects.get(pk=post_id)  # getting the liked posts
        m = Like(post=likedpost)  # Creating Like Object
        m.save()  # saving it to store in database
        return HttpResponse("Success!")  # Sending an success response
    else:
        return HttpResponse("Request method is not a GET")
