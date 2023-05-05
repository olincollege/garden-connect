"""
Creates a form where users may create new comments
"""
from django import forms
from comment.models import Comment # pylint: disable=E0401

class CommentForm(forms.ModelForm):
    """
    Uploadable data that is given by the user to make a new comment
	Attributes:
		body: A class instance representing a user input of a string
		of characters
	"""
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea'}), required=True)

    class Meta: # pylint: disable=R0903
        """
		Creating the formatting fields for creating a new post
		Attributes:
			model: A class representing an instance of a new comment
			being formed
			fields: A tuple showing the areas that are given by the
			user
		"""
        model = Comment
        fields = ('body',)
