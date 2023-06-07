from django.urls import path
from .views import *

app_name='streams'

urlpatterns = [
    path('streams/', StreamsApiView.as_view(), name='streams'),
    path('streams/<int:pk>', StreamApiView.as_view(), name='stream'),
    path('cdz/', CdzsApiView.as_view(), name='streams'),
    path('cdz/<int:pk>', CdzApiView.as_view(), name='stream'),

]