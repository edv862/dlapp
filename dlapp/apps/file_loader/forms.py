from django import forms


class FileUploadForm(forms.Form):
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
    number = forms.IntegerField(min_value=0, required=False)
    text_search = forms.CharField(required=False)

    class Meta:
        verbose_name = 'File upload form'

    def clean(self):
        cleaned_data = super(FileUploadForm, self).clean()

        # Either test search has a value or number has a value.
        if (cleaned_data['text_search'] == '') and (cleaned_data['number'] is None):
            self.add_error(
                None,
                'You must search either by text or by [line, paragraph].'
            )

        return cleaned_data
