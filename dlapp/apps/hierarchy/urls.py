from django.conf.urls import url

from .views import FileUploadHierarchyView, ConsultHierarchyView


app_name = 'hierarchy'
urlpatterns = [
    url(
        r'upload/$',
        FileUploadHierarchyView.as_view(),
        name='hierarchy_upload',
    ),
    url(
        r'consult/$',
        ConsultHierarchyView.as_view(),
        name='hierarchy_consult',
    ),
]
