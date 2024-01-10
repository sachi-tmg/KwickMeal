from django.urls import path

from customer_orders.views import HomePage,Menu,LoginPage,SignupPage,AboutPage, filter_food, order

urlpatterns = [
    path('',LoginPage,name='login'),
    path('signup/',SignupPage,name='signup'),
    path('home/',HomePage,name='home'),
    path('menu/',Menu,name='menu'), 
    path('about/',AboutPage,name='about'), 
    path('filter-food/<int:id>/',filter_food,name='filter_food'),  
    path('order/<int:id>/',order,name='order'),  
    # path('logout/', logout_view, name='logout'),




]