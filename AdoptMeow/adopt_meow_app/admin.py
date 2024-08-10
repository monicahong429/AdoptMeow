from django.contrib import admin

from .models import Adoption, Pet, User


class PetAdmin(admin.ModelAdmin):
  list_display = ('name', 'age', 'breed', 'adoption_status')
  search_fields = ('name', 'breed')
  list_filter = ('adoption_status', 'breed')

admin.site.register(User)
admin.site.register(Pet, PetAdmin)
admin.site.register(Adoption)