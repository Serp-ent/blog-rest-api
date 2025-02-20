from rest_framework import routers
from blog.views import (
    AuthorViewset,
    BlogViewset,
    CommentViewset,
    AuthTestView,
    UserRegistrationView,
)
from django.urls import path

router = routers.DefaultRouter()

router.register(r"authors", AuthorViewset, basename="author")
router.register(r"blogs", BlogViewset, basename="blog")
router.register(r"comments", CommentViewset, basename="comment")

urlpatterns = [
    path("authTest/", AuthTestView.as_view()),
    path(
        "register/",
        UserRegistrationView.as_view(),
        name="register",
    ),
]

urlpatterns += router.urls
