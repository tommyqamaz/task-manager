from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Status(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(_("Дата создания"), auto_now_add=True)

    class Meta(object):
        verbose_name = "status"
        verbose_name_plural = "statuses"

    def __str__(self):
        return self.name