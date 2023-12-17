from django.http import HttpResponse
from django.shortcuts import redirect,render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.http import JsonResponse
# Create your views here.

def HomePage(request):
    return render(request,'home.html')

def SignupPage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if the phone number is already in use
        if User.objects.filter(username=phone).exists():
            messages.error(request, 'Phone number is already in use. Please choose a different one.')
            return redirect('signup')  # Redirect back to the signup page

        # If the phone number is not in use, create a new user
        my_user = User.objects.create_user(phone, email, password)
        my_user.first_name = name
        my_user.last_name = name
        my_user.save()

        return redirect('login')

    return render(request, 'signup.html')


def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        user = authenticate(username=username,password=pass1)
        if user is None:
            messages.error(request, 'Invalid phone number or password')
        else:
            login(request,user)
            return redirect('home')
            
    return render(request,'login.html')




def phone(request):
    phone = request.POST.get('phone', '')
    check_for_signup = request.GET.get('check_for_signup', False)

    # Check if a user with the given phone number exists
    if get_user_model().objects.filter(phone=phone).exists():
        if check_for_signup:
            return JsonResponse({'message': 'This phone number is already registered.'}, status=400)
        else:
            return JsonResponse({'message': ''})
    else:
        return JsonResponse({'message': 'This phone number is available.'})
