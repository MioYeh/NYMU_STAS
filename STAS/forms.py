from django import forms 
from .models import *
  
class HotelForm(forms.ModelForm): 
    class Meta: 
        model = FORM_IMAGE
        # fields = ['name' , 'hotel_Main_Img'] 
        fields = ['Chart_No','Pathological_Section']