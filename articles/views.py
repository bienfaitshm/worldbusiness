from rest_framework import viewsets, mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.db.models import Count
from .models import Article, Magazine, Read, CategoryArticle, RubriqueMagazine
from .serializers import ArticleSerializer, MagazineSerializer, ReadSerializer, CategoryArticleSerializer, RubriqueMagazineSerializer


class RubriqueMagazineView(viewsets.ReadOnlyModelViewSet):
    queryset = RubriqueMagazine.objects.all()
    serializer_class = RubriqueMagazineSerializer


class CategoryArticleView(viewsets.ReadOnlyModelViewSet):
    queryset = CategoryArticle.objects.all()
    serializer_class = CategoryArticleSerializer


class ArticleView(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all().annotate(
        num_read=Count("read")).order_by("-created_at")
    serializer_class = ArticleSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category', 'edition_date', 'redactor']
    search_fields = ['title', 'description',
                     'content', 'redactor', 'category__name']


class ReadArticleView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Read.objects.all()
    serializer_class = ReadSerializer


class MagazineView(viewsets.ReadOnlyModelViewSet):
    queryset = Magazine.objects.all().prefetch_related(
        'docs').order_by("-created_at")
    serializer_class = MagazineSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['rubrique']
    search_fields = ['title', 'description']
