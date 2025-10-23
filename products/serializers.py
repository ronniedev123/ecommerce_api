from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    created_by_name = serializers.CharField(source='created_by.username', read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'created_by', 'created_by_name', 'created_at', 'updated_at']
        read_only_fields = ['created_by', 'created_at', 'updated_at']

