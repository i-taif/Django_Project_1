from django.urls import path
from . import views
from django.contrib.auth.views import LoginView , LogoutView
urlpatterns = [
    path('register/', views.register,name='register'),
    path('login/',LoginView.as_view(template_name='login.html'),name='login'),
    path('registeconsolt/',views.registercon,name='registeconsolt'),
    path('registerpage/',views.registerpage,name='registerpage'),
    path('logout/',LogoutView.as_view(template_name='userApp/logout.html'),name='logout')
]