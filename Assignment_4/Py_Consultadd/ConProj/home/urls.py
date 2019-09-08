
from django.urls import path
from home import views

urlpatterns = [
    path('index/', views.index, name = "index"),
    path('about/', views.about, name = "About"),
    path('gallery/', views.gallery, name = "Gallery"),
    path('login/', views.login, name = "Login"),
    path('signup/', views.signup, name = "Signup"),
]