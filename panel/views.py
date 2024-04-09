from .serializer import PanelSerializer
from rest_framework import viewsets
from .models import Panel


class PanelView(viewsets.ModelViewSet):
    serializer_class = PanelSerializer
    queryset = Panel.objects.all()
