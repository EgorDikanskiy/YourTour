from django.db import models
from catalog.models import Spot, Region
from django.core import validators
from catalog.validators import MaxWordsValidator
from ckeditor.fields import RichTextField
from django.utils import dateformat, timezone
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail


class Route(models.Model):
    user = models.ForeignKey(
        "users.User",
        verbose_name="пользователь",
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        verbose_name="название",
        max_length=150,
        validators=[validators.MaxLengthValidator(150)],
        help_text="Введите название",
    )
    text = RichTextField(
        verbose_name="Текст",
        help_text="Введите описание",
        validators=[MaxWordsValidator(1000)],
    )
    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        related_name="route_region",
        related_query_name="route_region",
        default=None,
        blank=True,
        null=True,
        verbose_name="Регион",
        help_text="Выберите или добавьте регион",
    )
    date_created = models.DateTimeField(
        verbose_name="дата создания маршрута",
        auto_now_add=True,
    )
    spots = models.ManyToManyField(
        Spot,
        verbose_name='места',
        help_text='Выберите или добавьте место',
    )
    class Meta:
        verbose_name = "маршрут"
        verbose_name_plural = "маршруты"


class RouteMainImage(models.Model):
    def upload_to(self, file_name):
        type_image = file_name.split(".")[1]
        return (
            f"reservoir/{self.route.user.id}/{self.route_id}/"
            f"{dateformat.format(timezone.now(), 'd_m_y_H_i', )}.{type_image}"
        )

    route = models.OneToOneField(
        "Route",
        on_delete=models.CASCADE,
        verbose_name="озеро",
        related_name="route_mainimage",
        related_query_name="route_mainimage",
    )

    image = models.ImageField(
        upload_to=upload_to,
        verbose_name="изображение",
    )

    @property
    def get_300x300px(self):
        return get_thumbnail(self.image, "300x300", crop="center", quality=51)

    def image_tmb(self):
        if self.image:
            return mark_safe(
                f"<img src=/media/{self.get_300x300px}/>",
            )
        return "Изображение не найдено/отсутсвует"

    @property
    def alter_img(self):
        if self.image:
            return f"{self.get_300x300px}"
        return None

    image_tmb.short_description = "превью"
    image_tmb.allow_tags = True

    fields = ["image_tmb"]

    def __str__(self):
        return self.image.url

    class Meta:
        verbose_name = "изображение"
        verbose_name_plural = "изображения"


class RouteImages(models.Model):
    def upload_to(self, file_name):
        type_image = file_name.split(".")[1]
        return (
            f"reservoir/{self.route.user.id}/{self.route_id}/"
            f"{dateformat.format(timezone.now(), 'd_m_y_H_i', )}.{type_image}"
        )

    route = models.ForeignKey(
        "Route",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="товар",
        related_query_name="route_images",
        related_name="route_images",
    )

    image = models.ImageField(
        upload_to=upload_to,
        null=True,
        blank=True,
        verbose_name="изображение",
    )

    @property
    def get_300x300px(self):
        return get_thumbnail(
            self.image,
            "300x300",
            crop="center",
            quality=51,
        )

    def image_tmb(self):
        if self.image:
            return mark_safe(
                f"<img src=/media/{self.get_300x300px}/>",
            )
        return "Изображение не найдено/отсутсвует"

    @property
    def alter_img(self):
        if self.image:
            return f"/media/{self.get_300x300px}"
        return None

    image_tmb.short_description = "превью"
    image_tmb.allow_tags = True

    fields = ["image_tmb"]

    def __str__(self):
        return self.image.url

    class Meta:
        verbose_name = "изображения"
        verbose_name_plural = "изображения"
