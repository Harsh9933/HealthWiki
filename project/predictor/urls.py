from django.urls import path
from predictor import views

urlpatterns = [
    path('',views.Predictor,name="home"),
    # path('user',views.Result,name="user")
]
