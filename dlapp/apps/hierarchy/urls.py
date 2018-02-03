from django.conf.urls import url

from .views import FileUploadHierarchyView


app_name = 'hierarchy'
urlpatterns = [
    url(
        r'upload/$',
        FileUploadHierarchyView.as_view(),
        name='hierarchy_upload',
    ),
]
