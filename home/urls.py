
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('HomeAPI', views.HomeAPIView)
router.register('LanguageAPI', views.LanguageView)
router.register('SettingAPI', views.SettingView)

urlpatterns = [

    path('', include(router.urls))
]