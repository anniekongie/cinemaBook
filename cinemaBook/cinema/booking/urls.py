from django.urls import path

from . import views
from django.conf.urls import url

urlpatterns = [
    path('signup/', views.SignUpFormView.as_view(), name='signup'),
]
