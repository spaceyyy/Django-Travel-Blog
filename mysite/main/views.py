from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    postlist = Post.objects.all()
    return render(request, 'templates/main/index.html', {'postlist':postlist})

def blog(request):
    postlist = Post.objects.all()
    return render(request, 'templates/main/blog.html', {'postlist': postlist})

def postdetails(request, pk):
    postlist = Post.objects.get(pk=pk)
    return render(request, 'templates/main/postdetails.html', {'postlist': postlist})