# Generated by Django 4.2.7 on 2023-11-09 05:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image/')),
                ('upload_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
