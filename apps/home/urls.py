from django.urls import path

from . import views

app_name = "home"

urlpatterns = [
    path("", views.index_view, name="home-index"),
    path("create_view/", views.create_view, name="create-item"),
]
