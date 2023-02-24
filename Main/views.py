from django.shortcuts import render
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from Main.models import Blogs
from Main.serializers import BlogSerializer

# Create your views here.

class blogViewSet(ModelViewSet):

    permission_classes = [permissions.IsAuthenticated] # We need this endpoint to consumed only upon authentication :

    serializer_class = BlogSerializer()
    def get_queryset(self):
        queryset = Blogs.objects.all()
        return queryset