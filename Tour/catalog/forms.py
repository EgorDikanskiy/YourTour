from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple

from catalog.models import Spot

__all__ = []

from django_filters import widgets


class SpotForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["images"].widget.attrs["multiple"] = True
        self.fields["images"].widget.attrs["required"] = False
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    images = forms.ImageField(
        label="Картинки",
        required=False,
    )

    class Meta:
        model = Spot
        exclude = (
            Spot.user.field.name,
            Spot.date_created.field.name,
            Spot.is_active.field.name,
        )
