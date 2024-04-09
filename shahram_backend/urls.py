from django.contrib import admin
from django.urls import path, include
from File.views import UploadViewSet
from selfie.views import SelfieView
from panel.views import PanelView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'music', UploadViewSet, basename="music")
router.register(r'selfie', SelfieView, basename="selfie")
router.register(r'panel', PanelView, basename="panel")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

]
