from django.urls import path


from . import views

app_name = 'labservice'

urlpatterns = [
    path('', views.labservice_list, name='list'),
    path('<int:pk>/', views.labservice_detail, name='detail'),
    path('<int:pk>/delete/', views.labservice_delete, name='delete'),
    path('<int:pk>/edit/', views.labservice_edit, name='edit'),
    path('add-service/', views.add_service, name='add_service'),
]