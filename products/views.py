from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Category
from .serializers import CategorySerializer
from .permissions import IsAdminUserRole

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUserRole()]
        return [permissions.AllowAny()]

# Create your views here.
