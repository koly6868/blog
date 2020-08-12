from django.shortcuts import render
from django.views import generic
from .models import Post
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.order_by('-pub_date')[:10]


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


def create_post_view(request):
    return render(request, 'blog/create_post.html')

def create_post(request):
    print(request.POST)
    return HttpResponse('ok')
