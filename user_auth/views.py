from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm, CustomAuthenticationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class UserLoginView(LoginView):
    template_name = 'signin.html'
    form_class = CustomAuthenticationForm

    def get_success_url(self):
        return reverse_lazy('index_view')


class UserLogoutView(LogoutView):

    def get_default_redirect_url(self):
        return '/'


