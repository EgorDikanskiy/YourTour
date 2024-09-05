from django.urls import include, path

from homepage import views

app_name = "homepage"

urlpatterns = [
    path(
        "",
        views.Home.as_view(),
        name="homepage",
    ), ]
