from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .form import UserSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User

class user_register(CreateView):
    model = User
    form_class = UserSignUpForm
    template_name = 'register.html'

    def form_valid(self, form):
        user = form.save()
        #login(self.request, user)
        return redirect('/login')

def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('/webapp/pd')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    form = AuthenticationForm()
    return render(request, 'login.html', context={'form':form})

def logout_view(request):
    logout(request)
    return redirect('/')

def page(request):
    return render(request, 'index.html', context={})
