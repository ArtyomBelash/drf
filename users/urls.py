from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.views import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(redirect_authenticated_user=True, form_class=AuthenticationForm,
                                     template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

