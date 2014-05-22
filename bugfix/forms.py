from django import forms


class RepairUploadForam(forms.Form):
    file  = forms.FileField()