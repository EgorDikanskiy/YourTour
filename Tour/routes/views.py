from django.views.generic import DetailView, ListView
from routes.models import Route
from django.shortcuts import render
from django.views.generic.edit import FormMixin

__all__ = []


class RoutesView(ListView):
    template_name = "routes/routes.html"

    def get(self, request):
        rotes = (
            Route.objects.only("name", "region")
        )
        context = {"rotes": rotes}
        return render(request, self.template_name, context)


class RouteDetailView(DetailView, FormMixin):
    model = Route
    template_name = "routes/detail.html"
    context_object_name = "route_info"
    pk_url_kwarg = "pk"
    context = {}

    def get(self, request, pk):
        route = self.model.objects.filter(id=pk)
        self.context["route_info"] = (
            route.first()
        )
        return render(request, self.template_name, self.context)
