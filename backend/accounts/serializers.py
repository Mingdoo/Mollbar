from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.utils.timezone import now
from movies.models import Rating


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'email')


class ProfileSerializer(serializers.ModelSerializer):
    days_since_joined = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'wishlist', 'date_joined', 'rating_set', 'days_since_joined')
    
    def get_days_since_joined(self, obj):
        return (now() - obj.date_joined).days + 1



class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('wishlist', )
