from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('signup', views.signupUser, name="signup"),
    path('upload', views.upload, name="upload"),
    path('<int:pk>', views.delete, name="delete"),
    path('deleteaccount', views.del_user, name="deleteaccount"),
]