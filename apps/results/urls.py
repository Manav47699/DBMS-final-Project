from django.urls import path
from . import views

app_name = 'results'

urlpatterns = [
    path('', views.result_list, name='list'),
    path('create/', views.result_create, name='create'),
    path('<int:pk>/edit/', views.result_update, name='update'),
    path('<int:pk>/delete/', views.result_delete, name='delete'),
]
