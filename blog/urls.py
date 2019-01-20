from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('posts', views.PostModelViewSet)

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('api/v1/', include(router.urls)),
    path('api/token/', views.CreateTokenView.as_view(), name='token'),
]