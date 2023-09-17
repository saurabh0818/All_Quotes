from django import forms
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={"placeholder": "Enter Full Name", "aria-label": "Full Name"}),
            'occupation': forms.TextInput(attrs={"placeholder": "Enter Author Profession", "aria-label": "occupation"}),


        }
        labels = {
            'name': "Enter Name ",
            'occupation': 'Profession ',

        }


class QuotesForm(forms.ModelForm):

    class Meta:
        model = Quote
        fields = '__all__'

        widgets = {
            'quotes': forms.TextInput(attrs={"placeholder": "Enter Your Quotes", "aria-label": "Quotes"}),
            'type_quotes': forms.TextInput(attrs={"placeholder": "Enter Quotes Type", "aria-label": "Type_Quotes"}),



        }
        labels = {
            'Author_Id': "Choose Your IDs ",
            'quotes':  "Enter Quotes",
            'type_quotes': 'Quotes Type ',

        }


class spcl_typeForm(forms.ModelForm):

    class Meta:
        model = spcl_type
        fields = '__all__'

        widgets = {
            'catagories': forms.TextInput(attrs={"placeholder": "Enter Your Cataogries", "aria-label": "Quotes"}),

        }
        labels = {
            'catagories':  "Enter Catagory",
            'images': 'Upload Your Image ',

        }


class SpecialMessageForm(forms.ModelForm):

    class Meta:
        model = SpecialMessages
        fields = '__all__'

        widgets = {
            'quotes': forms.TextInput(attrs={"placeholder": "Enter Your Quotes", "aria-label": "Quotes"}),
            'sub_type': forms.TextInput(attrs={"placeholder": "Ex : Mother, Father, Gf, Bf ", "aria-label": "Type_Quotes"}),



        }
        labels = {
            'quotes_type':  "Select Type Quotes",
            'quotes':  "Enter Quotes",
            'sub_type': 'Sub-Quotes Type ',

        }
