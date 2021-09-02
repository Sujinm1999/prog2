from django.urls import path
from . import views

urlpatterns = [
    path('',views.login,name='login'),
    path('register/', views.register, name='register'),
    # path('home/',views.home,name='home'),
    path('home/', views.task_view, name='task_view'),
    path('delete/<int:wishid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('covtask/',views.TaskListView.as_view(),name='covtask'),
    path('covdetail/<int:pk>/',views.TaskDetailView.as_view(),name='covdetail'),
    path('covupdate/<int:pk>/', views.TaskUpdateView.as_view(), name='covupdate'),
    path('covdelete/<int:pk>/',views.TaskDeleteView.as_view(),name='covdelete'),
]