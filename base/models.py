from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name  # Return the name of the category
    

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Making tags unique to avoid duplicate tags.

    def __str__(self):
        return self.name  # Return the name of the tag


class Post(models.Model):
    title = models.CharField(max_length=100)
    '''Add author field when adding author model and authentication feature'''
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Uncomment and use User model when ready.
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, blank=True)  # Allow blank for posts without tags.
    created_at = models.DateTimeField(auto_now_add=True)  # Corrected the typo (DataTimeField -> DateTimeField)
    '''Add updated_at field when implementing edit feature for blogs'''
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title # Return the title for better readability in the admin panel.
