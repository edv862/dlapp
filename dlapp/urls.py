from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(
        r'^file-loader/',
        include(
            'file_loader.urls',
            namespace='file-loader'
        )
    ),
    url(
        r'^file-loader-hierarchy/',
        include(
            'hierarchy.urls',
            namespace='hierarchy'
        )
    ),
    url(
        r'^user/',
        include(
            'user_management.urls',
            namespace='user'
        )
    ),
    url(
        r'^logout/$',
        LogoutView.as_view(),
        name='logout',
    ),
    url(
        r'^$',
        LoginView.as_view(template_name='home.html'),
        name='home',
    ),
]
