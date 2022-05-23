from django import forms
from .models import Relative
from django.db import models   
from django import forms  


class UserImage(forms.ModelForm):  
    class Meta:  
        # To specify the model to be used to create form  
        model = Relative
        # It includes all the fields of model  
        fields =  ("user", "relation", "image_url")
        

