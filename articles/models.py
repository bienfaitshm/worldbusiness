from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class CategoryArticle(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class RubriqueMagazine(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class BaseArticle(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="images")

    class Meta:
        abstract = True


class Article(BaseArticle):
    content = RichTextUploadingField()  # CKEditor Rich Text Field
    redactor = models.CharField(max_length=255)
    edition_date = models.DateTimeField()
    category = models.ForeignKey(
        CategoryArticle, on_delete=models.CASCADE, null=True, default=None)

    def __str__(self) -> str:
        return self.title


class Magazine(BaseArticle):
    rubrique = models.ForeignKey(
        RubriqueMagazine, on_delete=models.CASCADE, null=True, default=None)

    def __str__(self):
        return self.title


class Docs(BaseModel):
    magazine = models.ForeignKey(
        Magazine, on_delete=models.CASCADE, related_name="docs")
    files = models.FileField(upload_to="datas")

    def __str__(self):
        return self.files.name


class Read(BaseModel):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return f"Lecture du {self.article}"
