from django.shortcuts import render
from .models import Post

# Create your views here.
def blog(request):
  posts = Post.objects.all()
  return render(request, "Blog/blog.html", {"posts": posts})
