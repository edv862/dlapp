from django.conf.urls import url

from .views import UserRegisterView


app_name = 'user_namagement'
urlpatterns = [
    url(
        r'^register/',
        UserRegisterView.as_view(),
        name='register',
    )
]
