from django.urls import path
from usermanagement import views

urlpatterns=[
     path('register/',views.register, name='register'),
     path('customer_register/',views.customer_register.as_view(), name='customer_register'),
     path('sale_register/',views.saleperson_register.as_view(), name='saleperson_register'),
     path('login/',views.login_request, name='login'),
     path('logout/',views.logout_view, name='logout'),
]