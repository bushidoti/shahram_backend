# Generated by Django 5.0.3 on 2024-04-09 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Selfie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.FileField(blank=True, null=True, upload_to='static_media/media/pic/', verbose_name='عکس')),
            ],
            options={
                'verbose_name_plural': 'عکس ها',
            },
        ),
    ]