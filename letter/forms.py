from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', 
                               min_length=6, 
                               widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label='Password',
                               min_length=6,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class RegisterForm(forms.Form):
    username = forms.CharField(label='Username',
                               min_length=6,
                               widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(label='Email',
                               min_length=6,
                               widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(label='Password',
                               min_length=6,
                               widget=forms.TextInput(attrs={'placeholder': 'Password'}))
