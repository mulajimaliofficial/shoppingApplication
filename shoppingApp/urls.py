from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from shoppingApp.views import *

urlpatterns = [
    path('signup/', CreateAccount.as_view(), name="signup"),
    path('login/', LoginView.as_view(), name="login"),
    path('users/', ListUsers.as_view(), name="users"),
    path('update/', UpdateProfile.as_view(), name="update"),
    path('product/', MyProductView.as_view()),
    path('product/<int:pk>/', MyProductView.as_view()),
    path('forgot-password/',ForgotPasswordView.as_view()),
    path('set-password/',SetPasswordView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('change-password/',ChangePasswordView.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)