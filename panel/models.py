from django.db import models


class Panel(models.Model):
    bio = models.TextField("بیوگرافی", blank=True, null=True)
    spotify = models.TextField("لینک اسپاتیفای", blank=True, null=True)
    apple = models.TextField("لینک اپل موزیک", blank=True, null=True)
    youtube = models.TextField("لینک یوتیوب", blank=True, null=True)
    shazam = models.TextField("لینک شازم", blank=True, null=True)
    insta = models.TextField("لینک اینستاگرام", blank=True, null=True)
    pic = models.FileField("عکس پروفایل", upload_to='static_media/media/pic/', blank=True, null=True)
    biopic = models.FileField("عکس بیوگرافی", upload_to='static_media/media/pic/', blank=True, null=True)
    carousel1 = models.FileField("عکس اسلاید 1", upload_to='static_media/media/pic/', blank=True, null=True)
    carousel2 = models.FileField("عکس اسلاید 2", upload_to='static_media/media/pic/', blank=True, null=True)
    carousel3 = models.FileField("عکس اسلاید 3", upload_to='static_media/media/pic/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "پنل"

