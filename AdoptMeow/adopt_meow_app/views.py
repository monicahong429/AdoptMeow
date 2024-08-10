from django.shortcuts import render
from rest_framework import generics, permissions

from .models import Adoption, Pet, User
from .serializers import AdoptionSerializer, PetSerializer, UserSerializer

# Create your views here.

def index(request):
  return render(request, 'index.html')

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