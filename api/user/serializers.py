from api.user.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "date", "is_staff"]
        read_only_field = ["id"]
