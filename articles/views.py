from rest_framework import viewsets, mixins
from django.db.models import Count
from .models import Article, Magazine, Read
from .serializers import ArticleSerializer, MagazineSerializer, ReadSerializer


class ArticleView(viewsets.ModelViewSet):
    queryset = Article.objects.all().annotate(num_read=Count("read"))
    serializer_class = ArticleSerializer


class ReadArticle(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Read.objects.all()
    serializer_class = ReadSerializer


class MagazineView(viewsets.ModelViewSet):
    queryset = Magazine.objects.all()
    serializer_class = MagazineSerializer
