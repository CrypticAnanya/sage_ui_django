from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('ask/', views.ask_sage, name='ask_sage'),
    path('process_voice/', views.process_voice, name='process_voice'),
]
