from django.urls import path
from . import views

urlpatterns=[
    path('',views.home, name="home"),
    path('project/<str:pk>/',views.project,name="project"),
    path('add-project/', views.addProject,name="add-project"),
    path('edit-project/<str:pk>/', views.editProject,name="edit-project"),
    path('inbox/', views.inboxPage ,name="inbox"),
    path('message/<str:pk>/', views.messagePage ,name="message")
]