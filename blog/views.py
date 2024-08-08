from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    #render関数はクライアントからのリクエストに対して動的にHTMLを生成し、それをレスポンスとして返すための関数
    return render(request, 'blog/post_list.html', {'posts': posts})