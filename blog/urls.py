from rest_framework import routers
from blog.views import AuthorViewset, BlogViewset, CommentViewset

router = routers.DefaultRouter()

router.register(r"authors", AuthorViewset, basename="author")
router.register(r"blogs", BlogViewset, basename="blog")
router.register(r"comments", CommentViewset, basename="comment")

urlpatterns = router.urls
