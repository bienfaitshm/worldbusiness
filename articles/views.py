from rest_framework import viewsets
from django.db.models import Count
from .models import Article, Magazine, Read
from .serializers import ArticleSerializer, MagazineSerializer


class ArticleView(viewsets.ModelViewSet):
    queryset = Article.objects.all().annotate(num_read=Count("read"))
    serializer_class = ArticleSerializer


class MagazineView(viewsets.ModelViewSet):
    queryset = Magazine.objects.all()
    serializer_class = MagazineSerializer
