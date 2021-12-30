from rest_framework import serializers
from .models import User, Travel, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

    def create(self, validated_data):
        category = Category.objects.create(**validated_data)
        return category


class TravelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Travel
        fields = '__all__'

    def create(self, validated_data):
        travel = Travel.objects.create(**validated_data)
        return travel


class UserSerializer(serializers.ModelSerializer):
    travel = TravelSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
