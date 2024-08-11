from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')
def post_list(request):
    return render(request, 'posts/post_list.html', {})