from django.urls import path
from . import views


app_name = 'core'
urlpatterns = [
    path('',views.HomePage.as_view(),name='home'),
    path('question/<int:pk>/',views.QuestionDetail.as_view(),name='question-detail'),
]