from django.db.models import Model
from django.db.models import CharField, ImageField, PositiveIntegerField, ForeignKey, \
    DateTimeField, ManyToManyField, CASCADE

from users.models import User


class Ad(Model):
    """
    Описывает объявление
    """
    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.title

    title = CharField(null=True, db_index=True, max_length=100)
    price = PositiveIntegerField(null=True, db_index=True)
    description = CharField(null=True, blank=True, max_length=2000)
    image = ImageField(null=True, blank=True, upload_to="django_media")
    author = ForeignKey(User, null=True, on_delete=CASCADE)
    created_at = DateTimeField(null=True, auto_now_add=True)


class Comment(Model):
    """
    Описывает комментарий
    """
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return self.text

    text = CharField(null=True, db_index=True, max_length=200)
    ad = ForeignKey(Ad, null=True, on_delete=CASCADE)
    author = ForeignKey(User, null=True, on_delete=CASCADE)
    created_at = DateTimeField(null=True, auto_now_add=True)
