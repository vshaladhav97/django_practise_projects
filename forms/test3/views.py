from django.shortcuts import render
from .forms import StudentRegistration, StudentForm
from .models import Student
from .forms import JoinForm
from django.views.generic import FormView
from django.http import JsonResponse
# from .mixin import AjaxFormMixin
# Create your views here.


def showform(request):
    post = StudentRegistration()
    return render(request, 'enroll/students.html', {'form': post})


def studentview(request):
    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form1': form}
    # print(form.query)
    return render(request, 'enroll/studentdata.html', context)


class JoinFormView(FormView):

    form_class = JoinForm
    template_name = 'forms/ajax.html'
    success_url = '/form-success/'

    def form_invalid(self, form):
        response = super(JoinFormView, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super(JoinFormView, self).form_valid(form)
        print(form.cleaned_data)
        if self.request.is_ajax():
            print(form.cleaned_data)
            data = {
                'message': "Successfully submitted form data."
            }
            return JsonResponse(data)
        else:
            return response
