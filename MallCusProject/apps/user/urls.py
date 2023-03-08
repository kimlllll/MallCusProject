from django.urls import path
from . import views
urlpatterns = [
    #user
    path("register/",views.RegisterView.as_view()),

    path("uername/<username>/count/",views.UsernameCountView.as_view()),

]