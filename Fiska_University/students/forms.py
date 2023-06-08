from django import forms
from .models import Students_Data

class Students_Form(forms.ModelForm):
    class Meta:
        model = Students_Data
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Students_Form, self).__init__(*args, **kwargs)
        self.fields['major'].empty_label = "Select Major"
        self.fields['status'].empty_label = "Select Status"

    # def clean_sku(self):
    #     if self.instance: 
    #         return self.instance.nim
    #     else: 
    #         return self.fields['NIM']

class Students_Edit_Form(forms.ModelForm):
    NIM = forms.CharField(disabled=True)
    class Meta:
        model = Students_Data
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Students_Edit_Form, self).__init__(*args, **kwargs)
        self.fields['major'].empty_label = "Select Major"
        self.fields['status'].empty_label = "Select Status"