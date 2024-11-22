from django.shortcuts import render
from .models import Post, Category, Tag

# Create your views here.
def home(request):
    """
    Render the home page.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse object with the rendered home page.
    """

    posts = Post.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()


    context = {
        'posts': posts,
        'categories': categories,
        'tags': tags,
        }
    return render(request, 'home.html', context)

def createPost(request):
    return render(request, 'create_post.html')