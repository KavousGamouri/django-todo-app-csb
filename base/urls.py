from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'base'
urlpatterns = [
    path('login/',views.CustomLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='base:login'),name='logout'),
    path('register/',views.RegisterFormView.as_view(),name='register'),

    path('',views.TaskListView.as_view(),name='task-list'),
    path('task-detail/<int:pk>/',views.TaskDetailView.as_view(),name='task-detail'),
    path('create-task/',views.TaskCreateView.as_view(),name='create-task'),
    path('update-task/<int:pk>/',views.TaskUpdateView.as_view(),name='update-task'),
    path('delete-task/<int:pk>/',views.TaskDeleteView.as_view(),name='delete-task'),
]