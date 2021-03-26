from django.shortcuts import render
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.http.response import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import Permission
from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import Loan
from rest_framework.response import Response
from .serializers import LoanSerializer, LoanSerializer2
from rest_framework.views import APIView
from .decorators import unauthenticated_user


# # Create your views here.
@unauthenticated_user
def sign_up(request):
    """This function is used to perform sign up of user and assign group to the user."""
    form = SignUpForm(request.POST)
    if request.method == "POST":

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Account was created for ' + username)
            return HttpResponseRedirect('/')
    else:
        form = SignUpForm()
    return render(request, 'enroll/signup.html', {'form': form})


@unauthenticated_user
def user_login(request):
    """This function is used to perform login of existing user."""
    if request.method == 'POST':

        fm = AuthenticationForm(request=request, data=request.POST)

        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)

            if user is not None:
                login(request, user)
                group_permissions = list(Permission.objects.filter(
                    group__user=request.user).values("codename"))

                perm = []
                for group_permission in group_permissions:
                    perm.append(group_permission["codename"])

                return JsonResponse({'perm': perm}, status=200)
            else:
                messages.info(request, 'Username OR password is incorrect')
    else:
        fm = AuthenticationForm()

    return render(request, 'enroll/userlogin.html', {'form': fm})


def logoutUser(request):
    """This logoutUser() function is used to perform logout of existing user."""
    logout(request)
    return redirect('/')


class Management(APIView):
    def get(self, request):
        """Get tha Loan data."""

        loan = Loan.objects.all()
        
        serializer = LoanSerializer2(loan, many=True)
        
        return Response(serializer.data)

    def post(self, request):
        """Post loan data"""
        json_data = request.data
        loan = {"loan_amount": request.data["loan_amount"], "loan_duration": request.data["loan_duration"], "rate_of_interest": request.data["rate_of_interest"], "interest_amount": request.data["interest_amount"],
                "final_amount": request.data["final_amount"], "loan_limit": request.data["loan_limit"], "due_date": request.data["due_date"], "amt_paid_by_the_bank": request.data["amt_paid_by_the_bank"], "user_has_to_pay": request.data["user_has_to_pay"], "user_id": request.user.id}

        
        address = LoanSerializer(data=loan)
        
        if address.is_valid():
            address.save()

            return Response(address.data, status=200)
        else:
            return Response(address.data, status=400)


def client(request):
    """used to merge Management class to check and save loan details"""
    current_user = request.user
    user_name = current_user.username
    context = {'user_name': user_name}
    return render(request, "enroll/loan.html", context)


def client1(request):
    """used to show loan details with user details"""
    current_user = request.user
    user_name = current_user.username
    context = {'user_name': user_name}
    return render(request, "enroll/show_loan.html", context)
