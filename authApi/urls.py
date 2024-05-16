from unicodedata import name
from django.urls import path
from .views import (RegisterView, LoginUserView, LogoutApiView)
from rest_framework_simplejwt.views import (TokenRefreshView,)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', LoginUserView.as_view(), name='login-user'),
    path('logout/', LogoutApiView.as_view(), name='logout')
    ]