from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}) , required=False)
    first_name = forms.CharField(label="", max_length=200, widget= forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}, required=False))
    last_name = forms.CharField(label="" , max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}required=False))
    
class Meta:
    model = User
    fields = ('username', 'first_name', 'last_name','email','password1','password2')
    
def __init__(self, *args, **kwargs):
    super(SignUpForm, self).__init__(*args, **kwargs)
    
    self.fields['username'].widget.attrs['class']='form-control'
    self.fields['username'].widget.attrs['placeholder']= 'User Name'
    self.fields['username'].label=""
    self.fields['usename'].help_text= '<span class="form-text text-muted> samll">'
    
    self.fields['password1'].widget.attrs['class']='form-control'
    self.fields['password1'].widget.attrs['placeholder']= 'Password'
    self.fields['password1'].label=""
    self.fields['password1'].help_text= '<ul class="form-text text-muted> samll"><li>Your password cannot be too similar of other personal information</li><li>Your password must contain at least 8 character</ul>'
    
    self.fields['password2'].widget.attrs['class']='form-control'
    self.fields['password2'].widget.attrs['placeholder']= 'Confirmed Password'
    self.fields['password2'].label=""
    self.fields['password2'].help_text= '<ul class="form-text text-muted> samll"><li>Your password cannot be too similar of other personal information</li><li>Your password must contain at least 8 character</ul>'
    
    