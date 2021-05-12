from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView


app_name = 'accounts'
urlpatterns = [
    path('all/',views.Users.as_view()),
    path('get/<int:pk>/',views.UserDetail.as_view()),
    path('create/',views.CreateUser.as_view()),
    path('edit/<int:pk>/',views.EditUser.as_view()),
    path('remove/<int:pk>/',views.RemoveUser.as_view()),
    path('get-user-from-token/',views.GetUserFromToken.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]