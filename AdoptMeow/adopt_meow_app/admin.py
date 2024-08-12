from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Adoption, Favorite, Pet, User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
  list_display = ('username', 'email', 'role', 'create_date', 'update_date')
  search_fields = ('username', 'email')
  list_filter = ('role', 'create_date')
  fieldsets = (
    (None, {'fields': ('username', 'password')}),
    ('Personal info', {'fields': ('email', 'role')}),
    ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    ('Important dates', {'fields': ('last_login', 'date_joined')}),
  )

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
  list_display = ('name', 'age', 'breed', 'adoption_status', 'create_date', 'update_date')
  search_fields = ('name', 'breed')
  list_filter = ('adoption_status', 'breed', 'create_date')
  
@admin.register(Adoption)
class AdoptionAdmin(admin.ModelAdmin):
  list_display = ('user', 'pet', 'status', 'request_date', 'create_date', 'update_date')
  search_fields = ('user__username', 'pet__name')
  list_filter = ('status', 'create_date')

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
  list_display = ('user', 'pet', 'create_date', 'update_date')
  search_fields = ('user__username', 'pet__name')
  list_filter = ('create_date', 'user__username')