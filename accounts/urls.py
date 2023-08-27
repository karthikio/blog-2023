from django.urls import path
from .views import loginView, logoutView, registerView


urlpatterns = [
  path('login/', loginView, name='login_page'),
  path('register/', registerView, name='register_page'),
  path('logout/', logoutView, name='logout_page'),
]