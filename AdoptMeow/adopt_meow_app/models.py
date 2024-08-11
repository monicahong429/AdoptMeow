from django.contrib.auth.models import AbstractUser
from django.db import models


# Inherit from AbstractUser to use Django's built=in user authentication system
class User(AbstractUser):
  ROLE_CHOICES = [
    ('admin', 'Admin'),
    ('user', 'User'),
  ]
  # Add a role field with choices for admin and user
  role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
  create_date = models.DateTimeField(auto_now_add=True)
  update_date = models.DateTimeField(auto_now=True)
  
  groups = models.ManyToManyField(
    'auth.Group',
    related_name='custom_user_set',
    blank=True,
    help_text='The groups this user belongs to.',
    verbose_name='groups'
  )
  user_permissions = models.ManyToManyField(
    'auth.Permission',
    related_name='custom_user_permissions_set',
    blank=True,
    help_text='Specific permissions for this user.',
    verbose_name='user permissions'
  )

class Pet(models.Model):
  name = models.CharField(max_length=100)
  age = models.IntegerField()
  breed = models.CharField(max_length=100)
  health_records = models.TextField()
  adoption_status = models.BooleanField(default=False)
  additional_info = models.TextField(blank=True, null=True)
  image = models.ImageField(upload_to='pets/', blank=True, null=True)
  create_date = models.DateTimeField(auto_now_add=True)
  update_date = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.name

class Adoption(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
  request_date = models.DateTimeField(auto_now_add=True)
  status = models.CharField(max_length=20, choices=[
    ('pending', 'Pending'),
    ('approved', 'Approved'),
    ('rejected', 'Rejected'),
  ], default='pending')
  create_date = models.DateTimeField(auto_now_add=True)
  update_date = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return f"{self.user.username} {self.pet.name}"