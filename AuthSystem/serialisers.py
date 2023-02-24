from rest_framework.serializers import ModelSerializer
from AuthSystem.models import User


class SignupSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
        ]

class LoginSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
        ]