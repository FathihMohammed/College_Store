from django.urls import path, include
from . import views
app_name='CEMP_APP'
urlpatterns = [
    path('',views.home,name='homepage'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout,name='logout'),
    path('about/',views.about,name='about'),
    path('details/',views.details,name='details'),
]