from .serializer import MusicSerializer
from rest_framework import viewsets
from .models import Music
import django_filters


class MusicFilter(django_filters.rest_framework.FilterSet):
    name = django_filters.rest_framework.CharFilter(field_name='name', lookup_expr='contains')

    class Meta:
        model = Music
        fields = ['name']


class UploadViewSet(viewsets.ModelViewSet):
    serializer_class = MusicSerializer
    queryset = Music.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = MusicFilter
