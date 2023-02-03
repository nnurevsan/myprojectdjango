# Generated by Django 4.1.6 on 2023-02-03 21:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=144, verbose_name='Başlık')),
                ('aciklama', models.TextField(blank=True, null=True, verbose_name='Açıklama')),
                ('eklenme_tarihi', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Eklenme Tarihi')),
                ('durum', models.BooleanField(default=False, verbose_name='Yapıldı')),
            ],
        ),
    ]
