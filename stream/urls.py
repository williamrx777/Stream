from django.urls import path
from .views import *


urlpatterns = [
    path('', StreamsApiView.as_view(), name='streams'),
    path('streams/<int:pk>', StreamApiView.as_view(), name='stream'),

]