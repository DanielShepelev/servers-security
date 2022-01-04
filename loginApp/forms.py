from django import forms
from .models import User
from .models import SeasonCode
from loginApp.password_validator import password_custome_validate as validator


class login_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password')
        
    # def clean_password(self):
    #     password = self.cleaned_data.get('password')
    #     try:
    #         # password_validation.validate_password(password, self.instance)
    #         validator().validate(password)
    #     except forms.ValidationError as error: 
    #         return 'invalid messege'
    
class forgot_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ('password',)
        
    # def clean_password(self):
    #     password = self.cleaned_data.get('password')
    #     try:
    #         # password_validation.validate_password(password, self.instance)
    #         validator().validate(password)
    #     except forms.ValidationError as error: 
    #         return 'invalid messege'
        
        
class register_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email','password')        
        
    # def clean_password(self):
    #     password = self.cleaned_data.get('password')
    #     try:
            # password_validation.validate_password(password, self.instance)
            # validator().validate(password)
        # except forms.ValidationError as error: 
            # return 'Password legth at least of NUM with both numbers and symbols'