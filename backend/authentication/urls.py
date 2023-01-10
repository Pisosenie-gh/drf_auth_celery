
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from bot_api.urls import urlpatterns as bot_urls
from authentication.views import CreateUserView

app_name = 'authentication'


urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('users/create/', CreateUserView.as_view()),

]

urlpatterns += bot_urls
