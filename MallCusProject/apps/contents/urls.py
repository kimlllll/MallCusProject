from django.urls import path
from . import views

urlpatterns = [

    #contents
    path("index/",views.IndexView.as_view(),name='index'),

]