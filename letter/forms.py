from django import forms

class LoginForm(forms.Form):
    login_username = forms.CharField(label='Username', 
                               min_length=6, 
                               widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    login_password = forms.CharField(label='Password',
                               min_length=6,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class RegisterForm(forms.Form):
    regis_username = forms.CharField(label='Username',
                               min_length=6,
                               widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    regis_email = forms.EmailField(label='Email',
                               min_length=6,
                               widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    regis_password = forms.CharField(label='Password',
                               min_length=6,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class LetterForm(forms.Form):
    subject = forms.CharField(label='Subject',
                              max_length=100,
                              widget=forms.TextInput(attrs={'placeholder': 'Enter subject here.'}))
    message = forms.CharField(label='Message',
                              widget=forms.Textarea(attrs={'placeholder': 'Enter message here.'}))
    datetime = forms.DateTimeField(label='Send to',
                                  input_formats='%d/%m/%Y %H:%M',
                                  widget=forms.DateInput(attrs={'id':'datetimepicker', 'placeholder': 'dd/mm/yyyy hh:mm'}))
                              
