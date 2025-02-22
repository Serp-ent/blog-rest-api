from django.urls import include, path
from blog.views import Version2View

urlpatterns = [
    path("test/", Version2View.as_view()),
]
