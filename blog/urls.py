from rest_framework import routers
from drf_spectacular import views as docsViews
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
    path("schema/", docsViews.SpectacularAPIView.as_view(), name="schema"),
    path(
        "swagger/",
        docsViews.SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger",
    ),
    path(
        "redoc/",
        docsViews.SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]

urlpatterns += router.urls
