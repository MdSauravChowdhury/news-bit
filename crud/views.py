from django.shortcuts import render
from django.views.generic import DeleteView, UpdateView, CreateView
from news.models import Post

# Create your views here.
class PostCreate(CreateView):

    model = Post
    template_name = "create.html"
    fields = [
        'title', 'author', 'thumbnail', 'view_count', 'comment_count', 'text', 'category', 'featured'
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)


class PostUpdate(UpdateView):

    model = Post
    template_name = "create.html"
    fields = [
        'title', 'author', 'thumbnail', 'view_count', 'comment_count', 'text', 'category', 'featured'
    ]

    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False

  

class PostDelete(DeleteView):

    model = Post
    template_name = "create.html"
    success_url = 'index'

    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False 





