from django.urls import path
from . import views

app_name = 'iframes'

urlpatterns = [
        path("get_iframe/<str:name>", views.DashboardIframes.as_view()),
        path("get_iframe/", views.DashboardIframes.as_view()),
]
