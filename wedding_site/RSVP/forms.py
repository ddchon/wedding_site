from django import forms
from crispy_forms.helper import FormHelper
from . import models

class GuestForm1(forms.ModelForm):

    class Meta:
        model = models.Guest
        fields = "__all__"


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False


class GuestForm2(forms.ModelForm):

    class Meta:
        model = models.GuestParty
        fields = "__all__"
        widgets = {'guest': forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        form1 = kwargs['instance']
        form1.save()
        self.fields['guest'].initial = form1
        self.helper = FormHelper()
        self.helper.form_tag = False
