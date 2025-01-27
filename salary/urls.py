from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.SalaryViewSet)



urlpatterns = [
    path('salary', include(router.urls))
]