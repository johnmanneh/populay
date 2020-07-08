from django import forms

from manneh.models import Manneh

class MannehForm(forms.ModelForm):
     firstname        = forms.CharField(label='',required=True,
                       widget=forms.Textarea(
                       attrs={'placeholder':'First name'}
                         )
                       )
     surname          = forms.CharField(required=True,
                      widget=forms.Textarea(
                       attrs={'placeholder':'Last name'}
                        )
                      )
     member_fields    = forms.ChoiceField(
                       choices=Manneh.member_choice,
                       label="",
                       initial='',
                       widget=forms.Select(),
                       required = True)
     emptyList_fields = forms.ChoiceField(
                       choices=Manneh.emptyList,
                       label="",
                       initial='',
                       widget=forms.Select(),
                       required = True)
                       

     class Meta:
        model = Manneh
        fields = [
            'firstname',
            'surname',
            'member_fields',
            'emptyList_fields'
            ]
    
     def clean_title(self,*args,**kwargs):
        title = self.cleaned_data.get("firstname")
        if 'labeh' not in title:
            raise forms.ValidationError("This is not a valid title")
        else:
            return title
         


class RawMannehForm(forms.Form):
    firstname        = forms.CharField(label='',required=True,
                       widget=forms.Textarea(
                       attrs={'placeholder':'First name'}
                         )
                       )
    surname          = forms.CharField(required=True,
                      widget=forms.Textarea(
                       attrs={'placeholder':'Last name'}
                        )
                      )
    member_fields    = forms.ChoiceField(
                       choices=Manneh.member_choice,
                       label="",
                       initial='',
                       widget=forms.Select(),
                       required = True)
    emptyList_fields = forms.ChoiceField(
                       choices=Manneh.emptyList,
                       label="",
                       initial='',
                       widget=forms.Select(),
                       required = True)
                       
  