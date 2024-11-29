from django.shortcuts import render, redirect
from .models import Post, Category, Tag
from .forms import PostForm

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
    """
    Render the create post page.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse object with the rendered create post page.
    """
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') # redirect to the home page on successful submission
        else:
            return render(request, 'create_post.html', {'form': form})
    else:
        form = PostForm()
        return render(request, 'create_post.html', {'form': form})