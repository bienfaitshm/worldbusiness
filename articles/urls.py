from rest_framework.routers import DefaultRouter
from .views import ArticleView, MagazineView, CategoryArticleView, RubriqueMagazineView, ReadArticleView


router = DefaultRouter()
router.register(r'category', CategoryArticleView, basename='category')
router.register(r'rubric', RubriqueMagazineView, basename='rubric')
router.register(r'read', ReadArticleView, basename='read')
router.register(r'articles', ArticleView, basename='articles')
router.register(r'magazines', MagazineView, basename='magazines')
urlpatterns = router.urls
