from rest_framework import serializers
from .models import User, Pet, Adoption

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'username', 'email', 'role', 'create_date', 'update_date']
    
class PetSerializer(serializers.ModelSerializer):
  class Meta:
    model = Pet
    fields = ['id', 'name', 'age', 'breed', 'health_records', 'adoption_status', 'additional_info', 'create_date', 'update_date']

class AdoptionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Adoption
    fields = ['id', 'user', 'pet', 'request_date', 'status', 'create_date', 'update_date']