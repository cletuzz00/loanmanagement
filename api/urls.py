from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import routers
from api.views.auth import AuthTokenObtainPairView
from api.views.users import UserViewset
from api.views.loans import LoanViewset, ClientViewset, InterestRateViewset

router = routers.DefaultRouter()
router.register('users', UserViewset, basename='users')
router.register('loans', LoanViewset, basename='loans')
router.register('clients', ClientViewset, basename='clients')
router.register('interestrates', InterestRateViewset, basename='interestrates')


urlpatterns = [
    # JWT TOKEN URLS
    path('token/fetch/', AuthTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),   
]
