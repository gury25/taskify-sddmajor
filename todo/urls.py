from django.urls import path

from . import views
#url to pages
urlpatterns = [
    path('', views.home, name=""), #homepage 
    path('dashboard', views.dashboard, name="dashboard"), #dashboard
    path('calendar', views.calendar, name="calendar"), #calendar
    path("calendar_events", views.calendar_events, name="calendar_events"), #page with formatted tasks for calendar to read
    path('quotes', views.quotes, name="quotes"), #quotes


    

   
   
    #CRUD (create, read, update, delete) operations
    

    path('create-task', views.createTask, name="create-task"), #create task
    path('view-tasks', views.viewTask, name="view-tasks"), #view task
    path('update-task/<str:pk>/', views.updateTask, name="update-task"), #update task, <str:pk> creates a dynamic url based on what task is being updated
    path('delete-task/<str:pk>/', views.deleteTask, name="delete-task")
] 