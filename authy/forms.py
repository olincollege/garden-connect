"""
Creates a form where users may create new accounts
"""
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from authy.models import Profile # pylint: disable=E0401

def forbidden_user(username):
    """
    Checks to see if a given username while signing up has
    a conflicting keyword
    Args:
		username: A string represented the username of a given
        account intended on being created
    """
    forbidden_users = ['admin', 'css', 'js', 'authenticate', 'login',
		       'logout', 'administrator', 'root', 'email', 'user', 'join',
			   'sql', 'static', 'python', 'delete']
    if username.lower() in forbidden_users:
        raise ValidationError('Invalid name for user, this is a reserverd word.')

def invalid_user(username):
    """
    Checks to see if a given username while signing up has
    a conflicting character
    Args:
		username: A string represented the username of a given
        account intended on being created
    """
    if '@' in username or '+' in username or '-' in username:
        raise ValidationError('This is an Invalid user, Do not user these chars: @ , - , + ')

def unique_email(username):
    """
    Checks to see if a given username while signing up has
    a used email
    Args:
		username: A string represented the username of a given
        account intended on being created
    """
    if User.objects.filter(email__iexact=username).exists():
        raise ValidationError('User with this email already exists.')

def unique_user(username):
    """
    Checks to see if a given username while signing up has
    been taken
    Args:
		username: A string represented the username of a given
        account intended on being created
    """
    if User.objects.filter(username__iexact=username).exists():
        raise ValidationError('User with this username already exists.')

class SignupForm(forms.ModelForm):
    """
    Form used for creating an account
    Attributes:
        username: A class instance representing a string of the
        user's username
        email: A class instance representing a string of the
        user's email
        password: A class instance representing a string of the
        user's password
        confirm_password: A class instance representing a string of the
        user's password that must match with password
    """
    username = forms.CharField(widget=forms.TextInput(), max_length=30, required=True,)
    email = forms.CharField(widget=forms.EmailInput(), max_length=100, required=True,)
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput(),
                                       required=True, label="Confirm your password.")

    class Meta: # pylint: disable=R0903
        """
		Creating the formatting fields for creating a new user
		Attributes:
			model: A class representing an instance of a new user
			fields: A tuple showing the areas that are given by the
			user such as the username, email, and password
		"""
        model = User
        fields = ('username', 'email', 'password')

    def __init__(self, *args, **kwargs):
        """
		Checks to see if the inputs used are valid for
        signing up
		"""
        super(SignupForm, self).__init__(*args, **kwargs) # pylint: disable=R1725
        self.fields['username'].validators.append(forbidden_user)
        self.fields['username'].validators.append(invalid_user)
        self.fields['username'].validators.append(unique_email)
        self.fields['email'].validators.append(unique_user)

    def clean(self):
        """
        Returns an empty input html file for the user to put
        in after submitting the form
        Returns:
			An empty html file to be used again for user inputs
            if necessary
        """
        super(SignupForm, self).clean() # pylint: disable=R1725
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password != confirm_password:
            self._errors['password'] = self.error_class(['Passwords do not match. Try again'])
        return self.cleaned_data

class ChangePasswordForm(forms.ModelForm):
    """
    Form used for creating an account
    Attributes:
        id: A class instance representing a string of the
        user's username
        old_password: A class instance representing a string of the
        user's old password
        new_password: A class instance representing a string of the
        user's desired password
        confirm_password: A class instance representing a string of the
        user's new password that must match with the desired password
    """
    id = forms.CharField(widget=forms.HiddenInput())
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input is-medium'}),
                                   label="Old password", required=True)
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input is-medium'}),
                                   label="New password", required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input is-medium'}), label="Confirm new password", required=True)

    class Meta: # pylint: disable=R0903
        """
		Creating the formatting fields for creating a new user
		Attributes:
			model: A class representing an instance of a user
			fields: A tuple showing the areas that are given by the
			user such as the id and passwords
		"""
        model = User
        fields = ('id', 'old_password', 'new_password', 'confirm_password')

    def clean(self):
        """
        Returns an empty input html file for the user to put
        in after submitting the form
        Returns:
			An empty html file to be used again for user inputs
            if necessary
        """
        super(ChangePasswordForm, self).clean() # pylint: disable=R1725
        user_id = self.cleaned_data.get('id')
        old_password = self.cleaned_data.get('old_password')
        new_password = self.cleaned_data.get('new_password')
        confirm_password = self.cleaned_data.get('confirm_password')
        user = User.objects.get(pk=user_id)
        if not user.check_password(old_password):
            self._errors['old_password'] =self.error_class(['Old password do not match.'])
        if new_password != confirm_password:
            self._errors['new_password'] =self.error_class(['Passwords do not match.'])
        return self.cleaned_data

class EditProfileForm(forms.ModelForm):
    """
    Modeling the profile editing features for users of GardenConnect
    Attributes:
    	picture: A class instance representing an uploadably location for
        profile images
        first_name: A class instance representing a string of the
        user's first name
        last_name: A class instance representing a string of the
        user's last name
        location: A class instance representing a string of the
        user's location
        url: A class instance representing a string of the
        user's personal website
    """
    picture = forms.ImageField(required=False)
    first_name = forms.CharField(widget=forms.TextInput(), max_length=50, required=False)
    last_name = forms.CharField(widget=forms.TextInput(), max_length=50, required=False)
    location = forms.CharField(widget=forms.TextInput(), max_length=25, required=False)
    url = forms.URLField(widget=forms.TextInput(), max_length=60, required=False)
    profile_info = forms.CharField(widget=forms.TextInput(), max_length=260, required=False)

    class Meta: # pylint: disable=R0903
        """
		Creating the formatting fields for creating a new user
		Attributes:
			model: A class representing an instance of a given profile
			fields: A tuple showing the areas that are given by the
			user such as the picture, names, locations, and profile
            infomration of a user
		"""
        model = Profile
        fields = ('picture', 'first_name', 'last_name', 'location', 'url', 'profile_info')
        