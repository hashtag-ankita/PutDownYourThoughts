from django.forms import ModelForm, CharField, TextInput, Textarea, ValidationError, ModelChoiceField, Select
from .models import Post, Category, Tag

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'tags']

    title = CharField(
        widget=TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter the title',
        })
    )

    content = CharField(
        widget=Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter the content',
        })
    )

    category = ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Select a category",
        widget=Select(attrs={
            'class': 'form-control',
        })
    )

    tags = CharField(
        required=False,
        widget=TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter tags separated by commas',
        })
    )

    def clean_tags(self):
        '''Optional: Validate and process the tags field.'''
        tags_input = self.cleaned_data.get('tags', '')
        tags_list = [tag.strip() for tag in tags_input.split(',') if tag.strip()]
        return tags_list # return a list of clean tags
    
    # def clean_category(self):
    #     '''Optional: Validate and process the category field.'''
    #     category_input = self.cleaned_data.get('category', '').strip()

    #     # Remove single or double quotes around the input if present
    #     if category_input.startswith(("'", '"')) and category_input.endswith(("'", '"')):
    #         category_input = category_input[1:-1].strip()

    #     if not category_input:
    #         raise ValidationError("Category cannot be empty!")
    #     return category_input.lower() # return the clean category