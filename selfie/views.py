from .serializer import SelfieSerializer
from rest_framework import viewsets
from .models import Selfie


class SelfieView(viewsets.ModelViewSet):
    serializer_class = SelfieSerializer
    queryset = Selfie.objects.all()
