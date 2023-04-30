from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add , name='add'),
    path('<int:id>/edit/', views.edit , name='edit'),
    path('<int:id>/delete/', views.delete, name='delete'),
    path('<int:id>/toggleDone/', views.toggleDone, name='toggleDone'),
]
