from django.contrib import admin
from .models import Music
from django_jalali.admin.filters import JDateFieldListFilter


class MusicAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = (
        ('release', JDateFieldListFilter),
    )
    search_fields = (
        "name",
    )


admin.site.register(Music, MusicAdmin)
