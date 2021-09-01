from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("abel", views.abel, name="abel"),
    path("david", views.david, name="david")
]
