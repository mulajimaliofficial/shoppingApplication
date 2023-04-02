from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from shoppingApp.views import *

urlpatterns = [
    path('create/', CreateAccount.as_view(), name="create_user"),
    path('login/', LoginView.as_view(), name="login"),
    path('users/', ListUsers.as_view(), name="users"),
    path('update/', UpdateProfile.as_view(), name="update"),
    path('product/', MyProductView.as_view()),
    path('product/<int:pk>/', MyProductView.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)