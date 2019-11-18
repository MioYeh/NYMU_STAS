from django.db import models

# Create your models here.
class FORM_IMAGE(models.Model): 
    Chart_No = models.CharField(max_length=50 ) 
    Pathological_Section = models.ImageField(upload_to='images/') 
