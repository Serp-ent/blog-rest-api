from rest_framework import routers
from blog.views import AuthorViewset

router = routers.DefaultRouter()

router.register(r'authors', AuthorViewset, basename='author')

urlpatterns = router.urls