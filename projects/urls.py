from django.urls import path, include
from rest_framework import routers

from projects import views

router = routers.DefaultRouter()
router.register(r'projects', views.ProjectListViewSet)
router.register(r'projects', views.ProjectDetailViewSet)
router.register(r'styles', views.StyleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('email/send/', views.send_mail),
]
