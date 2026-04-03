from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # Authentication endpoints
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    
    path('', views.getRoutes),

    path('projects/', views.getProjects),           # ✅ list
    path('projects/<str:pk>/', views.getProject),   # ✅ detail
    path('projects/<str:pk>/vote/', views.projectVote),   # ✅ vote
]