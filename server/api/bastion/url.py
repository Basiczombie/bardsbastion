from django.urls import path, include
from django.conf import settings
from bastion.views import *

urlpatterns = [
    path('', BastionView.as_view(), name='home'),
]
