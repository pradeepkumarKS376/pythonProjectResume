from django import forms
from .models import Personaldetailsmodels
from .models import *

# Create your views here.
###
# class personaldetailsForm(forms.Form):
#     Freelances = (("A","Available"), ("NA", "Non Available"),)
# Freelances = models.TextChoices('Available', 'Non Available')
# Date_of_Birth = forms.DateField()
# Website = forms.CharField(max_length=30)
# Phone = forms.CharField(max_length=15)
# City = forms.CharField(max_length=254)
# Degree = forms.CharField(max_length=254)
# Email = forms.EmailField(max_length=254)
# Freelance = forms.ChoiceField(choices=Freelances)
# Freelance = models.CharField(blank=True, choices=Freelances, max_length=15)


class PersonaldetailsForm(forms.ModelForm):
    class Meta:
        model = Personaldetailsmodels
        fields = "__all__"


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ("file",)
        # fields = "__all__"


class ContactForm(forms.ModelForm):
    class Meta:
        model = Personaldetailsmodels
        fields = "__all__"
