from django.urls import path
from .views import *

urlpatterns = [
    path("",Home,name="home"),
    path("about/",About,name="about"),
    path("contact/",Contact,name="contact"),
    path("check_result/<str:res_id>/",show_result,name="check_result"),
]
