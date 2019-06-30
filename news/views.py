from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View, ListView, DetailView
from .models import Post, EmailSubcribe

# Create your views here.
class IndexView(View):
    
    def get(self, request, *args, **kwargs):

        featured = Post.objects.filter(featured=True)
        latest = Post.objects.order_by('-timestamp')[:4]
        last = Post.objects.all().order_by('-timestamp')[:1]
        post = Post.objects.all().order_by('-timestamp')

        context = {
            'featured':featured,
            'latest':latest,
            'last':last,
            'post':post
        }
        return render(request, 'index.html', context)

class SinglePost(DetailView):
    
    model = Post
    template_name = "single-post.html"


class PostListView(ListView):

    model = Post
    template_name = "archive-page.html"   
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        most_resent_post = Post.objects.order_by('-timestamp')[:4]
        context["resent_post"] = most_resent_post
        context['page_request_var'] = "page"
        
        return context


'''    
def subcribe(request):

    if request.method == "POST":
        form = request.POST["email"]

        new_sub = EmailSubcribe()
        new_sub.email = form
        new_sub.save()
        
        return redirect('index')
    else:
        form = form()    
    return render(request, 'archive-page.html',{'form':form})
'''