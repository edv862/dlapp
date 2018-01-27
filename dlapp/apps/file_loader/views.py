from django.shortcuts import render, render_to_response
from django.urls import reverse_lazy
from django.core.files.uploadedfile import UploadedFile
from django.contrib.auth.models import User
from django.views.generic import FormView, TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from .reader import extract
from .word_search import word_search
from .forms import FileUploadForm
from .models import *


class FileUploadView(LoginRequiredMixin, FormView):
    form_class = FileUploadForm
    template_name = 'file-form.html'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            type_output = form.cleaned_data['search_for']
            number_to_look = form.cleaned_data['number']
            text = form.cleaned_data['text_search']
            usuario = self.request.user
            output_id = []

            # Proccesing the files.
            for file_input in request.FILES.getlist('file'):
                # Look for text, only in doc or txt.
                if text != '':
                    output = word_search(
                        text,
                        file_input
                    )
                    # Search type is text search.
                    search_type = Output.TEXT
                    search_value = text

                # Or look for the line or paragraph.
                else:
                    # Type output: 1 for line search, 2 for paragraph.
                    if type_output == '1':
                        search_type = Output.LINE
                    elif type_output == '2':
                        search_type = Output.PARAGRAPH

                    search_value = number_to_look
                    output = extract(
                        file_input, 
                        type_output,
                        number_to_look
                    )

                file = Output(
                    owner=usuario,
                    date=datetime.now(),
                    file_name=file_input.name,
                    output_text=output,
                    search_type=search_type,
                    search_value=search_value,
                )
                file.save()
                output_id.append(file.pk)

            self.success_url = reverse_lazy(
                'file-loader:output',
                kwargs={'output_id': output_id}
            )
            return super(FileUploadView, self).form_valid(form)
        else:
            return self.form_invalid(form)


class FileOutputView(LoginRequiredMixin, TemplateView):
    template_name = "file-output.html"

    def get_context_data(self, **kwargs):
        key_string = self.kwargs['output_id']
        nkey_string = key_string.replace("[", "").replace("]", "")
        keys = [int(s) for s in nkey_string.split(',')]

        file_list = []
        for key in keys:
            file_list.append(Output.objects.all().filter(pk=key)[0])

        kwargs['output'] = file_list

        return super(FileOutputView, self).get_context_data(**kwargs)


class OutputListView(LoginRequiredMixin, ListView):
    model = Output
    context_object_name = 'output'
    template_name = 'output-list.html'

    def get_queryset(self):
        return Output.objects.filter(owner=self.request.user)
