from django.urls import path
from . import views

urlpatterns = [
    path("login/",views.loginUser,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('register/',views.registerUser,name="register"),

    path("",views.list,name="list"),
    path("item/<str:pk>/",views.item,name="item"),
    path("create-task/",views.createTask,name="create-task"),
    path("update-task/<str:pk>/",views.updateTask,name="update-task"),
    path("delete-task/<str:pk>/",views.deleteTask,name="delete-task"),

]