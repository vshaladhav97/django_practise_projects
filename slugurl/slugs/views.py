from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.


def posts_list(request):
    all_posts = Post.objects.all()
    return render(request,
                    "enroll/post_list.html",
                    context={"all_posts": all_posts})


def posts_detail(request, slug):
    unique_slug = get_object_or_404(Post, slug=slug)
    # unique_slug = Post.objects.filter(slug=slug)
    # post = {'name':unique_slug, 'id':slug, 'name'}
    return render(request, "enroll/post_detail.html", {"post": unique_slug})

def urldetail(request, slug):
    detail = Post.objects.filter(slug=slug)
    student = {'id': slug, 'name': detail,
                'ids': 'this is id number {}'.format(slug)}
    return render(request, 'enroll/show2.html', student)