from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import FormView
import requests


class RegisterView(FormView):
    form_class = UserCreationForm
    model = User
    template_name = 'users/register.html'
    success_url = reverse_lazy('index')
    http_method_names = ['post', 'get']

    def form_valid(self, form):
        http_response = super().form_valid(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        url = 'http://127.0.0.1:8000/drf/api/v1/register/'
        data = {'username': username, 'password': password}
        requests_response = requests.post(url, json=data)
        if requests_response.status_code == 201:
            user = authenticate(username=username, password=password)
            login(self.request, user)
        return http_response
