from django import forms
from .models import SearchValues


class FileUploadHierarchyForm(forms.Form):
    file = forms.FileField(
        widget=forms.ClearableFileInput(
            attrs={
                'multiple': True,
            }
        )
    )

    class Meta:
        verbose_name = 'File upload form'


class ConsultUsagePartIdHierarchyForm(forms.ModelForm):

    class Meta:
        model = SearchValues
        fields = (
            'usage', 'part',
        )
