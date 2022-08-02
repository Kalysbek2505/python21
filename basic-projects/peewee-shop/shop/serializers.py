from dataclasses import field
from abstract.serializers import BaseSerializer
from .models import Product, Comment


class ProductSerializer(BaseSerializer):
    class Meta:
        fields = ('id', 'category', 'title', 'price', 'description')
        model = Product

class CommentSeralizer(BaseSerializer):
    class Meta:
        fields = ('id', 'user', 'body', 'created_at')
        model = Comment
