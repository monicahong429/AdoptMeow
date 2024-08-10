from django.urls import path

from . import views
from .views import (AdoptionCreateView, AdoptionListView, LoginUserView,
                    PetDetailView, PetListView, RegisterUserView,
                    UserDetailView)

urlpatterns = [
  path('', views.index, name='index'),
  path('api/register/', RegisterUserView.as_view(), name='register'),
  path('api/login/', LoginUserView.as_view(), name='login'),
  path('api/user/', UserDetailView.as_view(), name='user-detail'),
  path('api/pets/', PetListView.as_view(), name='pet-list'),
  path('api/pets/<int:id>/', PetDetailView.as_view(), name='pet-detail'),
  path('api/adoptions/', AdoptionCreateView.as_view(), name='adoption-create'),
  path('api/adoptions/', AdoptionListView.as_view(), name='adoption-list'),
]