from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import generics, permissions

from .forms import LoginForm, RegisterForm
from .models import Adoption, Favorite, Pet, User
from .serializers import AdoptionSerializer, PetSerializer, UserSerializer

# Create your views here.

User = get_user_model()

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

@login_required
def dashboard(request):
  return render(request, 'dashboard.html')

@login_required
def pet_detail(request, pet_id):
  pet = get_object_or_404(Pet, id=pet_id)
  user = User.objects.get(id=request.user.id)
  # favorites = Favorite.objects.filter(user=user)
  # return render(request, 'pet_detail.html', {'pet': pet, 'favorites': favorites})
  return render(request, 'pet_detail.html', {'pet': pet})

@login_required
def toggle_favorite(request, pet_id):
  pet = get_object_or_404(Pet, id=pet_id)
  user = User.objects.get(id=request.user.id)
  favorite, created = Favorite.objects.get_or_create(user=user, pet=pet)
  if not created:
    favorite.delete()
  return redirect('pet_detail', pet_id=pet_id)

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