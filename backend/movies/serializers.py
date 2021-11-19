from rest_framework import serializers
from .models import Genre, Movie, Rating


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


# class ReviewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Review
#         fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'
        read_only_fields = ('user', 'movie', )


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class MovieDetailSerializer(serializers.ModelSerializer):
    ratings = RatingSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'


"""
{
    "movie_id": 666235,
    "title": "샹치와 텐 링즈의 전설
    ...
    "ratings": {
        {"pk": 1, "user": 3, "rate": 8, "review": "마블의 새로운 시작이네요."},
        {"pk": 2, "user": 5, "rate": 5, "review": "별로였어요."},
        ...
    }
}
"""