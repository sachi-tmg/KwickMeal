from django.shortcuts import redirect,render
from django.contrib.auth.models import User
from customer_orders.models import Burger, Breakfast,Dinner,Drink,Dessert,Snack,Pizza,Customer,Reservation
from django.contrib import messages
from django.http import HttpResponse
from .models import Customer
from django.contrib.auth.hashers import make_password

# Create your views here.

def SignupPage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if the phone number is already in use
        if Customer.objects.filter(phone_no=phone).exists():
            messages.error(request, 'Phone number is already in use. Please choose a different one.')
            return redirect('signup')  # Redirect back to the signup page

        # Check if the email is already in use
        if Customer.objects.filter(email=email).exists():
            messages.error(request, 'Email is already in use. Please use a different email address.')
            return redirect('signup')  # Redirect back to the signup page

        # If the phone number and email are not in use, create a new customer
        hashed_password = (password)
        my_customer = Customer(customer_name=name, phone_no=phone, email=email, password=hashed_password)
        my_customer.save()

        return redirect('login')

    return render(request, 'signup.html')

  # Adjust the import path based on your project structure

def LoginPage(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        phone_no = request.POST.get('phone_no')
        password = request.POST.get('password')
        error_message = None

        # Check if a customer with the provided phone_no and password exists
        customer_exists = Customer.objects.filter(phone_no=phone_no, password=password).exists()

        if customer_exists:
            return redirect('home')
        else:
            messages.error(request, 'Wrong Phone no or Password.')

        return render(request, 'login.html')

def HomePage(request):
    return render(request,'home.html')

def Menu(request):
    burgers = Burger.objects.all()  # Move this line outside of the if statement
    breakfast = Breakfast.objects.all()
    dinner=Dinner.objects.all()
    drink=Drink.objects.all()
    dessert=Dessert.objects.all()
    snack=Snack.objects.all()
    pizza=Pizza.objects.all()
    

    if request.method == 'POST':
        # Any additional logic for handling POST requests can go here
        print(burgers)

    return render(request, 'menu.html', context= {'burgers': burgers, 'breakfast':breakfast,'dinner':dinner,'drink':drink,'dessert':dessert,'snack':snack,'pizza':pizza})


def AboutPage(request):
    return render(request,'about.html')

def reservation(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')
        No_of_guest = request.POST.get('guests')

        new_reservation = Reservation(
            name=name,
            email=email,
            phone=phone,
            date=date,
            time=time,
            No_of_guest=No_of_guest,
        )
        new_reservation.save()
        return HttpResponse("Successfully created")
        # You can also redirect to a success page or do something else after saving

    return render(request, 'reservation.html')

