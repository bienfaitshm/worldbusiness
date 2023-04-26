from rest_framework.routers import DefaultRouter
from .views import ArticleView, MagazineView


router = DefaultRouter()
router.register(r'articles', ArticleView, basename='articles')
router.register(r'magazines', MagazineView, basename='magazines')
urlpatterns = router.urls
