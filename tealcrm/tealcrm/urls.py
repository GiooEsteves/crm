from django.contrib import admin
from django.urls import path
from django.contrib import views

from core.views import index, about
from userprofile.views import signup

urlpatterns = [
    path('', index, name = 'index'),
    path('about/', about, name = 'about'),
    path('sign-up/', signup, name = 'signup'),
    path('log-in/', views.LoginView().as_view(template_name='userprofile/login.html'), name = 'login'),
    path('admin/', admin.site.urls),
]
