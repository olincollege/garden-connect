"""
Creates a form where users may create new posts
"""
from django import forms
from post.models import Post # pylint: disable=E0401

class NewPostForm(forms.ModelForm):
    """
    Uploadable data that is given by the user to make a new post

	Attributes:
		content: A class instance representing an uploadable images
		caption: A class instance representing a user input of a string
		of characters
		tags: A class instance representing a set of strings a user can
		put in
	"""
    content = forms.FileField(widget=
                              forms.ClearableFileInput(attrs={'multiple': True}), required=True)
    caption = forms.CharField(widget=
                              forms.Textarea(attrs={'class': 'input is-medium'}), required=True)
    tags = forms.CharField(widget=
                           forms.TextInput(attrs={'class': 'input is-medium'}), required=True)

    class Meta: # pylint: disable=R0903
        """
		Creating the formatting fields for creating a new post

		Attributes:
			model: A class representing an instance of a new post
			being formed
			fields: A tuple showing the areas that are given by the
			user such as the post data, post text, and post tags
		"""
        model = Post
        fields = ('content', 'caption', 'tags')
        