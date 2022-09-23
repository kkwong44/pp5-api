from rest_framework import generics, permissions
from .models import Category
from .serializers import CategorySerializer


class CategoryList(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Category.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
