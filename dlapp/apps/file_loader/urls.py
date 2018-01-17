from django.conf.urls import url

from .views import FileUploadView, FileOutputView, OutputListView


app_name = 'file_loader'
urlpatterns = [
    url(
        r'upload/$',
        FileUploadView.as_view(),
        name='upload',
    ),
    url(
        r'output/(?P<output_id>.+)/$',
        FileOutputView.as_view(),
        name='output',
    ),
    url(
        r'output/$',
        OutputListView.as_view(),
        name='output-list',
    ),
]
