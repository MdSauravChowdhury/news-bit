from django.urls import path

from .import views

urlpatterns = [
    path('create/post/', views.PostCreate.as_view(), name="post")
]
