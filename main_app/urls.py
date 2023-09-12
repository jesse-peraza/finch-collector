from django.urls import path
from . import views
urlpatterns = [
    path('', views.about, name='about'),
    path('finches/', views.finches_index, name='index'),
]
