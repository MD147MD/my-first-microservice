from django.urls import path
from . import views


app_name = 'question'
urlpatterns = [
    path('all/',views.GetAll.as_view()),
    path('get/<int:pk>/',views.GetQuestion.as_view()),
    path('create/',views.CreateQuestion.as_view()),
    path('edit/<int:pk>/',views.EditQuestion.as_view()),
    path('remove/<int:pk>/',views.RemoveQuestion.as_view())
]