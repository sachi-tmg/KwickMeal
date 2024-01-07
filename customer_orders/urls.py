from django.urls import path

from customer_orders.views import HomePage,Menu,LoginPage,SignupPage,AboutPage,reservation

urlpatterns = [
    
    path('',HomePage,name='home'),
    path('menu/',Menu,name='menu'),
    path('login/',LoginPage,name='login'),
    path('signup/',SignupPage,name='signup'),
    path('about/',AboutPage,name='about'),  
    path('reservation/',reservation,name='reservation'),    
]