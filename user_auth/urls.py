from django.urls import path
from .views import SignUpView, UserLoginView, UserLogoutView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]
