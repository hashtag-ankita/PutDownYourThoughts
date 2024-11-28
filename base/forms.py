from django.forms import ModelForm, CharField, TextInput, Textarea, ValidationError
from .models import Post, Category, Tag

class PostForm(ModelForm):
    # Tags field to accept CSV input for multiple tags
    tags = CharField(
        required=False,
        widget=TextInput(attrs={
            'class' : 'form-control',
        })
    )

    # Category field to allow dynamic input (searchable with datalist)
    category = CharField(
        required=True,
        widget=TextInput(attrs={
            'list': 'category-options', # For associating with the datalist
            'class' : 'form-control',
        })
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'tags'] # Exclude author
        widgets = {
            'title' : TextInput(attrs={
                'class' : 'form-control',
            }),
            'content' : Textarea(attrs={
                'class' : 'form-control',
                'rows' : 10,
            }),
        }

    def clean_tags(self):
        '''Optional: Validate and process the tags field.'''
        tags_input = self.cleaned_data.get('tags', '')
        tags_list = [tag.strip() for tag in tags_input.split(',') if tag.strip()]
        return tags_list # return a list of clean tags
    
    def clean_category(self):
        '''Optional: Validate and process the category field.'''
        category_input = self.cleaned_data.get('category', '').strip()

        # Remove single or double quotes around the input if present
        if category_input.startswith(("'", '"')) and category_input.endswith(("'", '"')):
            category_input = category_input[1:-1].strip()

        if not category_input:
            raise ValidationError("Category cannot be empty!")
        return category_input.lower() # return the clean category