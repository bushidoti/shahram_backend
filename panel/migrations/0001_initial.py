# Generated by Django 5.0.3 on 2024-04-09 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Panel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, null=True, verbose_name='بیوگرافی')),
                ('spotify', models.TextField(blank=True, null=True, verbose_name='لینک اسپاتیفای')),
                ('apple', models.TextField(blank=True, null=True, verbose_name='لینک اپل موزیک')),
                ('youtube', models.TextField(blank=True, null=True, verbose_name='لینک یوتیوب')),
                ('pic', models.FileField(blank=True, null=True, upload_to='static_media/media/pic/', verbose_name='عکس پروفایل')),
                ('carousel1', models.FileField(blank=True, null=True, upload_to='static_media/media/pic/', verbose_name='عکس اسلاید 1')),
                ('carousel2', models.FileField(blank=True, null=True, upload_to='static_media/media/pic/', verbose_name='عکس اسلاید 2')),
                ('carousel3', models.FileField(blank=True, null=True, upload_to='static_media/media/pic/', verbose_name='عکس اسلاید 3')),
            ],
            options={
                'verbose_name_plural': 'پنل',
            },
        ),
    ]
