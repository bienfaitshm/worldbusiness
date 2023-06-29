from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from django.db.models import Count

# Register your models here.
from .models import Docs, Article, Magazine, Read

admin.site.register(Read)
admin.site.register(Docs)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["pk", "title", "description", "num_read", "edition_date"]

    @admin.display(description="Nombre de lecture")
    def num_read(self, obj: Article):
        return obj.num_read  # type: ignore

    def get_queryset(self, request: HttpRequest) -> QuerySet[Article]:

        return Article.objects.all().annotate(num_read=Count("read"))

    def save_model(self, request, obj: Article, form, change) -> None:
        return super().save_model(request, obj, form, change)


@admin.register(Magazine)
class MagazineAdmin(admin.ModelAdmin):
    list_display = ["pk", "title", "description",  "num_docs"]

    @admin.display(description="Documents Lies")
    def num_docs(self, obj: Magazine):
        return obj.docs

    def get_queryset(self, request: HttpRequest) -> QuerySet[Magazine]:

        return Magazine.objects.all().annotate(num_docs=Count("docs"))

    def save_model(self, request, obj: Magazine, form, change) -> None:
        return super().save_model(request, obj, form, change)
