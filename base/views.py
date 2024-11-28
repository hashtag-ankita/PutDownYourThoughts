from django.shortcuts import render
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
    form = PostForm(request.POST)
    if request.method == 'POST':

        if form.is_valid():
            post = form.save(commit=False)

            # Add tags to the post
            tags_list = form.cleaned_data['tags']
            for tag_name in tags_list:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                post.tags.add(tag)

            # add category to the post
            category_name = form.cleaned_data.get('category')  # Get the category name from the form and normalize it
            category, created = Category.objects.get_or_create(name=category_name)  # Get or create a Category instance

            post = Post(
                title=form.cleaned_data['title'],
                content=form.cleaned_data['content'],
                category=category,
                author=request.user,
            )
            post.save()

            return render(request, 'post_created.html', {'post': post})
        
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'form': form,
    }
    
    return render(request, 'create_post.html', context)