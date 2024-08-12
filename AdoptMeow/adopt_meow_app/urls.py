from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views
from .views import (AdoptionCreateView, AdoptionListView, LoginUserView,
                    PetDetailView, PetListView, RegisterUserView,
                    UserDetailView)

urlpatterns = [
  # Web views
  path('', views.index, name='index'),
  path('login/', views.login_view, name='login_view'),
  path('logout/', LogoutView.as_view(next_page='index'), name='logout_view'),
  path('register/', views.register_view, name='register_view'),
  path('dashboard/', views.dashboard, name='dashboard'),
  path('pets/<int:pet_id>/', views.pet_detail, name='pet_detail'),
  path('toggle_favorite/<int:pet_id>/', views.toggle_favorite, name='toggle_favorite'),
  # REST Framework API
  path('api/login/', LoginUserView.as_view(), name='login-api'),
  path('api/register/', RegisterUserView.as_view(), name='register-api'),
  path('api/user/', UserDetailView.as_view(), name='user-detail-api'),
  path('api/pets/', PetListView.as_view(), name='pet-list-api'),
  path('api/pets/<int:id>/', PetDetailView.as_view(), name='pet-detail-api'),
  path('api/adoptions/', AdoptionCreateView.as_view(), name='adoption-create-api'),
  path('api/adoptions/', AdoptionListView.as_view(), name='adoption-list-api'),
]