from django.db import models

# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class BaseArticle(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="images")

    class Meta:
        abstract = True


class Article(BaseArticle):
    content = models.TextField(blank=True)
    redactor = models.CharField(max_length=255)
    edition_date = models.DateTimeField()

    def __str__(self) -> str:
        return self.title


class Docs(BaseModel):
    files = models.FileField(upload_to="datas")


class Magazine(BaseArticle):
    docs = models.ForeignKey(Docs, on_delete=models.CASCADE)


class Read(BaseModel):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
