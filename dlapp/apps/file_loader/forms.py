from django import forms


class FileUploadForm(forms.Form):
    line = "ln"
    parag = "pg"
    TYPE_CHOICES = (
        (line, 'Line'),
        (parag, 'Paragraph'),
    )

    choice_type = forms.ChoiceField(
        choices=TYPE_CHOICES,
        required=True
    )

    file = forms.FileField(
        widget=forms.ClearableFileInput(
            attrs={
                'multiple': True,
            }
        )
    )

    class Meta:
        verbose_name = 'File upload form'
