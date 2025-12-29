from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = "self/post_list.html"
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = Post
    template_name = "self/post_detail.html"
    context_object_name = "post"


class PostCreateView(CreateView):
    model = Post
    template_name = "self/post_create.html"
    fields = ['title', 'content']


class PostUpdateView(UpdateView):
    model = Post
    template_name = "self/post_update.html"
    fields = ['title', 'content']


class PostDeleteView(DeleteView):
    model = Post
    template_name = "self/post_delete.html"
    context_object_name = "post"
    success_url = reverse_lazy('post_list')
