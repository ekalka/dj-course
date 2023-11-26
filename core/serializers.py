from rest_framework import serializers
from .models import Profile, Post

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

    def validate_id_user(self, value):
        if value < 0:
            raise serializers.ValidationError("ID пользователя должен быть положительным числом.")
        return value

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'