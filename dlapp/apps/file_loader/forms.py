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

    search_for = forms.ChoiceField(
        choices=[(1, "Line"), (2, "Paragraph")]
    )

    number = forms.IntegerField(min_value=0)

    class Meta:
        verbose_name = 'File upload form'
