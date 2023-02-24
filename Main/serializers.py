from Main.models import Blogs
from Main.serializers import AuthorSerializer
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from AuthSystem.models import User


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'bio',
        ]


class BlogSerializer(ModelSerializer):
    
    class Meta:
        model = Blogs
        fields = [
            'title',
            'content',
            'date_created',
            'author',
        ]
