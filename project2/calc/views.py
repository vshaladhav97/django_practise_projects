# from calc import urls
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.base import TemplateView, RedirectView, DetailView
from calc.models import Post

# # Create your views here.
def index(request):
    # return HttpResponse("hello")
    # return render(request, 'home.html)
    # return render(request, 'home.html', {'name':"vishal"})
    context = {'name':'Vishal', 'course':'python', 'company':'v2stechnology'}
    return render(request, 'home.html', context)

def about(request):
    context = {'name':'Vishal', 'course':'python', 'company':'v2stechnology'}
    return render(request, 'about.html', context)


class Myview(View):
    name = 'vishal'
    # name = ''
    def get(self, request):
        # return HttpResponse('<h1>class Based View</h1>')
        return HttpResponse(self.name)
    
class Mychild(Myview):
    def get(self, request):
        return HttpResponse(self.name)
    
    
# def contactfun(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data['name'])
#             return HttpResponse('Thank you form submitted !!')
#     else:
#         form = ContactForm()   
#         return render(request, 'contact.html', {'form':form})

# class Ex2View(TemplateView):
    
#     template_name = "ex2.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['posts'] = Post.objects.get(id=1)
#         context['data'] = "Context Data for Ex2"
#         return context

# class HomeTemplateView(TemplateView):
#     template_name = 'homes.html'

class HomeTemplateView(TemplateView):
    template_name = 'homes.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context = {'name':'Vishal', 'rollno':101}
        context['name'] = 'vishal'
        context['rollno'] = 101
        return context
    
    
class HomeRedirectView(RedirectView):
    url = 'https://geekyshows.com'
    
    
class HomeDetailView(DetailView):
    template_name = 'homes.html'
    abc['name'] = 'vishal'
    abcd['rollno'] = 101