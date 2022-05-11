from django.urls import path
from usermanagement import views

urlpatterns=[
     path('register/',views.user_register.as_view(), name='register'),
     path('login/',views.login_request, name='login'),
     path('logout/',views.logout_view, name='logout'),
     path('',views.page, name='page')
]