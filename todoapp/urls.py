from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name="home"),
    path('about/', views.About, name="about"),
    path('services/', views.Services, name="services"),
    path('contact/', views.Contact, name="contact"),
    path('signup/', views.Signup, name="signup"),
    path('todo-list/', views.task_list, name="task_list"), 
    path('task/new', views.task_create, name="task_create"),
    path('task/delete/<int:task_id>/', views.task_delete, name="task_delete"),
    
]