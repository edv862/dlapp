from django.shortcuts import render
from .forms import FileUploadHierarchyForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import FormView
from .handle_file import get_heirarchy
from .models import *


# Create your views here.
class FileUploadHierarchyView(LoginRequiredMixin, FormView):
    form_class = FileUploadHierarchyForm
    template_name = 'file-hierarchy-form.html'
    success_url = reverse_lazy('hierarchy:hierarchy_upload')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            csv_file = request.FILES['file']
            json_heirarchy = get_heirarchy(csv_file)

            saveHeirarchy(json_heirarchy[0], json_heirarchy[1])

            self.success_url = reverse_lazy(
                'hierarchy:hierarchy_upload'
            )

            return super(FileUploadHierarchyView, self).form_valid(form)
        else:
            return self.form_invalid(form)


def saveHeirarchy(heirarchies, search_values):

    json_heirarchy_id_name = {}
    for value_heirarchy, json_heirarchy in heirarchies.items():
        value_heirarchy_obj = HierarchyValue.objects.get_or_create(value=value_heirarchy)
        for (name_heirarchy, array_row) in json_heirarchy.items():
            name_heirarchy_obj = \
                HierarchyName.objects.get_or_create(name=name_heirarchy, hierarchy_value=value_heirarchy_obj[0])

            for row in array_row:
                if row not in json_heirarchy_id_name:
                    json_heirarchy_id_name[row] = []
                json_heirarchy_id_name[row].append(name_heirarchy_obj[0].id)

    for row, array_search_values in search_values.items():
        if (len(array_search_values) == 2):
            search_values_obj =\
                SearchValues.objects.get_or_create(
                    usage=int(float(array_search_values[0])), value=int(float(array_search_values[1])))
            if row in json_heirarchy_id_name:
                for id_hierarchy_name in json_heirarchy_id_name[row]:
                    part_usage_hierarchy_name_obj =\
                        PartUsageHierarchyName.objects.get_or_create(
                            hierarchy_name_id=id_hierarchy_name,
                            search_value=search_values_obj[0]
                        )
