from django.urls import path
from .views import index, create,go


urlpatterns = [
    path("", index, name="home"),
    path("create", create, name="create"),
    path("<str:pk>", go, name="go")
]
