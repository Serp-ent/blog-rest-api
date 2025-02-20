from rest_framework import routers
from blog.views import AuthorViewset, BlogViewset

router = routers.DefaultRouter()

router.register(r"authors", AuthorViewset, basename="author")
router.register(r"blogs", BlogViewset, basename="blog")

urlpatterns = router.urls
