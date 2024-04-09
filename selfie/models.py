from django.db import models


class Selfie(models.Model):
    pic = models.FileField("عکس", upload_to='static_media/media/pic/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "عکس ها"

