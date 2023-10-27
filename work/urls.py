from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('convert_to_pdf/', views.convert_to_pdf, name='convert_to_pdf'),
    path('download_file/', views.download_file, name='download_file'),
    path('admin/', admin.site.urls),
]