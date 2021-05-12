from django.urls import path
from . import views


app_name = 'question'
urlpatterns = [
    path('create-question/',views.CreateQuestion.as_view(),name='create-question'),
    path('remove-question/<int:pk>/',views.RemoveQuestion.as_view(),name='remove-question'),

]