from django.urls import path

from . import views

app_name = 'client'
urlpatterns = [
    path('new_client', views.new_client, name='new_client'),
    path('<int:id>/create/branch', views.create_client_branch, name='create_branch'),
    path('<int:id>/delete/', views.delete_client, name='delete_client'),
    path('<int:id>/update/', views.update_client, name='update_client'),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]