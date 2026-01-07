from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register, name='register'),
    path('login/', views.login2, name='login'),
    path('profile/', views.setProfile, name='profile'),
    path('logout/', views.logout2, name='logout'),

    path('allTasks/', views.allTasks, name='allTasks'),      # עמוד כל המשימות
    path('tasks/add/', views.task_add, name='task_add'),     # הוספת משימה
    path('tasks/edit/<int:task_id>/', views.task_edit, name='task_edit'),   # עריכת משימה
    path('tasks/delete/<int:task_id>/', views.task_delete, name='task_delete'), # מחיקת משימה
    path('tasks/take/<int:task_id>/', views.take_task, name='take_task'),       # לקיחת משימה
    path('tasks/complete/<int:task_id>/', views.complete_task, name='complete_task'), # סמן כהושלמה
]
