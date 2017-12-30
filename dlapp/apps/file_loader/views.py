from django.shortcuts import render
from django.urls import reverse_lazy
from django.core.files.uploadedfile import UploadedFile
from django.contrib.auth.models import User
from django.views.generic import FormView, TemplateView
from datetime import datetime
from .forms import FileUploadForm
from .models import *
from .reader import extract


class FileUploadView(FormView):
    form_class = FileUploadForm
    template_name = 'file-form.html'
    success_url = reverse_lazy('file-loader:output')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            type_output = form.cleaned_data['search_for']
            number_to_look = int(form.cleaned_data['number'])
            usuario = User.objects.all()[0]

            # Proccesing the files.
            for file_input in request.FILES.getlist('file'):
                text_parsed = extract(
                    file_input,
                    type_output,
                    number_to_look
                )
                output(
                    owner=usuario,
                    date=datetime.now(),
                    output_text=text_parsed
                ).save()

            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class FileOutputView(TemplateView):
    template_name = 'file-output.html'
    context_object_name = 'output'
