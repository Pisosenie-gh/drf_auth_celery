
from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from authentication.views import CreateUserView

app_name = 'authentication'

urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('users/create/', CreateUserView.as_view()),
]