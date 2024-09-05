from django.contrib import admin

import routes.models


class ImageInline(admin.TabularInline):
    model = routes.models.RouteMainImage
    readonly_fields = (
        "id",
        routes.models.RouteMainImage.image_tmb,
    )
    extra = 1


class ImagesInline(admin.TabularInline):
    model = routes.models.RouteImages
    readonly_fields = (
        "id",
        routes.models.RouteImages.image_tmb,
    )

__all__ = []

@admin.register(routes.models.Route)
class RouteAdmin(admin.ModelAdmin):
    inlines = (
        ImageInline,
        ImagesInline,
    )
    fields = (
        routes.models.Route.name.field.name,
        routes.models.Route.text.field.name,
        routes.models.Route.region.field.name,
        routes.models.Route.date_created.field.name,
        routes.models.Route.spots.field.name,
    )
    readonly_fields = (routes.models.Route.date_created.field.name,)

    list_display = (
        routes.models.Route.name.field.name,
        routes.models.Route.region.field.name,
        routes.models.Route.date_created.field.name,
    )
    list_display_links = (routes.models.Route.name.field.name,)

    def save_model(
        self,
        request,
        obj,
        form,
        change,
    ):
        form_save = form.save(commit=False)
        form_save.user = request.user
        form_save.save()

        return super().save_model(request, obj, form, change)
