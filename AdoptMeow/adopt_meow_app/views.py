from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect, render
from rest_framework import generics, permissions

from .forms import LoginForm, RegisterForm
from .models import Adoption, Pet, User
from .serializers import AdoptionSerializer, PetSerializer, UserSerializer

# Create your views here.

def index(request):
  return render(request, 'index.html')

def login_view(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user = authenticate(request, username=username, password=password)
      if user is not None:
        login(request, user)
        return redirect('dashboard')
      else:
        form.add_error(None, 'Invalid usrname or password')
  else:
    form = LoginForm()
  return render(request, 'login.html', {'form': form})

def register_view(request):
  if request.method == 'POST':
    form = RegisterForm(request.POST)
    if form.is_valid():
      user = form.save(commit=False)
      user.set_password(form.cleaned_data['password'])
      user.save()
      login(request, user)
      return redirect('dashboard')
  else:
    form = RegisterForm()
  return render(request, 'register.html', {'form': form})

def dashboard(request):
  return render(request, 'dashboard.html')

class RegisterUserView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  
class LoginUserView(generics.GenericAPIView):
  # Implement login logic here
  pass

class UserDetailView(generics.RetrieveAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [permissions.IsAuthenticated]
  
class PetListView(generics.ListCreateAPIView):
  queryset = Pet.objects.all()
  serializer_class = PetSerializer
  
class PetDetailView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Pet.objects.all()
  serializer_class = PetSerializer
  permission_classes = [permissions.IsAdminUser]
  
class AdoptionCreateView(generics.CreateAPIView):
  queryset = Adoption.objects.all()
  serializer_class = AdoptionSerializer

class AdoptionListView(generics.ListAPIView):
  queryset = Adoption.objects.all()
  serializer_class = AdoptionSerializer
  permission_classes = [permissions.IsAdminUser]