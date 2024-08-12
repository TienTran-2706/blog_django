from django.shortcuts import render
from .models import Post
from media.models import Media


def create_post(request):
    if request.method == "POST":
        post = Post.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            
        )
def post_list(request):
    return render(request, 'posts/post_list.html', {})