from django.shortcuts import render
from .forms import FileUploadHierarchyForm, ConsultUsagePartIdHierarchyForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import FormView
from .handle_file import get_hierarchy
from .models import *
from django.http import JsonResponse


# Create your views here.
class FileUploadHierarchyView(LoginRequiredMixin, FormView):
    form_class = FileUploadHierarchyForm
    template_name = 'file-hierarchy-form.html'
    success_url = reverse_lazy('hierarchy:hierarchy_consult')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            csv_file = request.FILES['file']
            json_hierarchy = get_hierarchy(csv_file)

            saveHierarchy(json_hierarchy[0], json_hierarchy[1])

            return super(FileUploadHierarchyView, self).form_valid(form)
        else:
            return self.form_invalid(form)


class ConsultHierarchyView(LoginRequiredMixin, FormView):
    model = SearchValues
    form_class = ConsultUsagePartIdHierarchyForm
    template_name = 'consult-hierarchy.html'

    def get_context_data(self, **kwargs):
        context = super(ConsultHierarchyView, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        part = request.POST['part']
        usage = request.POST['usage']
        data = {}
        try:
            search_value = SearchValues.objects.get(usage=usage, part=part)

            return JsonResponse(getNamesValues(search_value))
        except SearchValues.DoesNotExist:
            try:
                search_value = SearchValues.objects.get(usage=part, part=usage)
                return JsonResponse(getNamesValues(search_value))
            except SearchValues.DoesNotExist:
                return JsonResponse(data)


def saveHierarchy(hierarchies, search_values):
    json_hierarchy_id_name = {}
    for value_hierarchy, json_hierarchy in hierarchies.items():
        value_hierarchy_obj = HierarchyValue.objects.get_or_create(
            value=value_hierarchy
        )
        for (name_hierarchy, array_row) in json_hierarchy.items():
            name_hierarchy_obj = \
                HierarchyName.objects.get_or_create(
                    name=name_hierarchy,
                    hierarchy_value=value_hierarchy_obj[0]
                )

            for row in array_row:
                if row not in json_hierarchy_id_name:
                    json_hierarchy_id_name[row] = []
                json_hierarchy_id_name[row].append(name_hierarchy_obj[0].id)

    for row, array_search_values in search_values.items():
        if (len(array_search_values) == 2):
            search_values_obj =\
                SearchValues.objects.get_or_create(
                    usage=int(float(array_search_values[0])), part=int(float(array_search_values[1])))
            if row in json_hierarchy_id_name:
                for id_hierarchy_name in json_hierarchy_id_name[row]:
                    PartUsageHierarchyName.objects.get_or_create(
                        hierarchy_name_id=id_hierarchy_name,
                        search_value=search_values_obj[0]
                    )


def getNamesValues(search_value):
    data = {}
    hierarchy_search_values = PartUsageHierarchyName.objects.filter(
        search_value=search_value
    )
    if hierarchy_search_values:
        for hierarchy_search_value in hierarchy_search_values:
            value = hierarchy_search_value.hierarchy_name.hierarchy_value.value
            if value not in data:
                data[value] = ""
            data[value] = hierarchy_search_value.hierarchy_name.name

        return data
    return None
