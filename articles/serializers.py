from rest_framework import serializers
from .models import Article, Magazine, Docs, Read, RubriqueMagazine, CategoryArticle


class RubriqueMagazineSerializer(serializers.ModelSerializer):
    class Meta:
        model = RubriqueMagazine
        fields = "__all__"


class CategoryArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryArticle
        fields = "__all__"


class DocSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docs
        fields = "__all__"


class ReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Read
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    num_read = serializers.IntegerField(read_only=True, default=0)

    class Meta:
        model = Article
        fields = "__all__"


class MagazineSerializer(serializers.ModelSerializer):
    docs = DocSerializer(many=True, default=[], )

    class Meta:
        model = Magazine
        fields = "__all__"
