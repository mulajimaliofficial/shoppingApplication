from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from shoppingApp.views import *

urlpatterns = [
    path('product/', MyProductView.as_view()),
    path('product/<int:user_id>/', MyProductView.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)