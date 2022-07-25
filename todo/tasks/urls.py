from django.urls import path
from .views import index, update_task, delete_task

urlpatterns = [
    path('', index, name='list'),
    path('update/<int:pk>/', update_task, name='update'),
    path('delete/<int:pk>/', delete_task, name='delete'),


]