from django.urls import path
from .import views
from .models import EmailSubcribe

urlpatterns = [
    path('index/', views.IndexView.as_view(), name="index"),
    path('post-list/', views.PostListView.as_view(), name="post_list"),
    path('single/post/<int:pk>/', views.SinglePost.as_view(), name="single"),
    # path('subcribe/', views.subcribe, name="sub")
]
