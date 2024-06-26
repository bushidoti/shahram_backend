from django.db import models
from django_jalali.db import models as jmodels
import jdatetime
from django.core.validators import MinLengthValidator


class Music(models.Model):
    name = models.CharField("نام آهنگ", blank=True, null=True, max_length=50)
    description = models.CharField("توضیحات", blank=True, null=True, max_length=300,
                                   validators=[MinLengthValidator(70)])
    release = jmodels.jDateField(verbose_name="تاریخ انتشار", default=jdatetime.date.today())
    spotify = models.TextField("لینک اسپاتیفای این آهنگ", blank=True, null=True)
    shazam = models.TextField("لینک شازم این آهنگ", blank=True, null=True)
    apple = models.TextField("لینک اپل موزیک این آهنگ", blank=True, null=True)
    youtube = models.TextField("لینک یوتیوب این آهنگ", blank=True, null=True)
    music = models.FileField("فایل آهنگ", upload_to='static_media/media/music/', blank=True, null=True)
    pic = models.FileField("فایل کاور", upload_to='static_media/media/pic/', blank=True, null=True)
    video = models.FileField("فایل موزیک ویدئو", upload_to='static_media/media/video/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "موزیک ها"

    def _str_(self):
        return self.name
