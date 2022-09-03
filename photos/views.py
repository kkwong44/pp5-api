from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from pp5_api.permissions import IsOwnerOrReadOnly
from .models import Photo
from .serializers import PhotoSerializer


class PhotoList(generics.ListCreateAPIView):
    serializer_class = PhotoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Photo.objects.all()
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'post',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

