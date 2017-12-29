from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(
        r'^file-loader/',
        include(
            'file_loader.urls',
            namespace='file-loader'
        )
    ),
]
