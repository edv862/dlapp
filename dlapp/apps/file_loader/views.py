from django.shortcuts import render
from django.urls import reverse_lazy
from django.core.files.uploadedfile import UploadedFile

from django.views.generic import FormView, TemplateView
from .forms import FileUploadForm


class FileUploadView(FormView):
    form_class = FileUploadForm
    template_name = 'file-form.html'
    success_url = reverse_lazy('file-loader:output')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():

            # Proccesing the files.
            for file_input in request.FILES.getlist('file'):
                print(file_input)
                # parser = PDFParser(file_input)
                # print(parser)

            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class FileOutputView(TemplateView):
    template_name = 'file-output.html'
    context_object_name = 'output'
