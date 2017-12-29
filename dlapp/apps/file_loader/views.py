from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import FormView, TemplateView
from .forms import FileUploadForm


class FileUploadView(FormView):
    form_class = FileUploadForm
    template_name = 'file-form.html'
    success_url = reverse_lazy('file-loader:output')


class FileOutputView(TemplateView):
    template_name = 'file-output.html'
    context_object_name = 'output'
