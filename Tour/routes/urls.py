from django.urls import path
from routes import views

app_name = "routes"

urlpatterns = [
    path(
        "",
        views.RoutesView.as_view(),
        name="routes",
    ),
    path(
        "<int:pk>",
        views.RouteDetailView.as_view(),
        name="route_detail",
    ),
]
