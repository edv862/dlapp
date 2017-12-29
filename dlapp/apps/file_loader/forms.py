from django import forms


class FileUploadForm(forms.Form):
    file = forms.FileField(
    )

    class Meta:
        verbose_name = 'File upload form'
