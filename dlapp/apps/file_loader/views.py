from django.shortcuts import render, render_to_response
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

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            type_output = form.cleaned_data['search_for']
            number_to_look = int(form.cleaned_data['number'])
            usuario = User.objects.all()[0]
            output_id = []

            # Proccesing the files.
            for file_input in request.FILES.getlist('file'):
                text_parsed = extract(
                    file_input,
                    type_output,
                    number_to_look
                )
                file = output(
                    owner=usuario,
                    date=datetime.now(),
                    output_text=text_parsed
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


class FileOutputView(TemplateView):
    def get(self, request, *args, **kwargs):
        """ Get necesary data to make the function work. """
        context = self.get_context_data(**kwargs)
        return render_to_response('file-output.html', context)

    def get_context_data(self, **kwargs):
        key_string = self.kwargs['output_id']
        nkey_string = key_string.replace("[", "").replace("]", "")
        keys = [int(s) for s in nkey_string.split(',')]

        file_list = []
        for key in keys:
            file_list.append(output.objects.all().filter(pk=key)[0])

        kwargs['output'] = file_list

        return super(FileOutputView, self).get_context_data(**kwargs)
