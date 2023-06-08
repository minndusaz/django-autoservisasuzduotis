# Generated by Django 4.2.1 on 2023-06-07 08:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('autoservisasinfo', '0012_automobiliomodelis_car_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commented_at', models.DateTimeField(auto_now_add=True, verbose_name='Commented')),
                ('content', models.TextField(max_length=4000, verbose_name='content')),
                ('commentator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_reviews', to=settings.AUTH_USER_MODEL, verbose_name='Commentator')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='autoservisasinfo.uzsakymas', verbose_name='order')),
            ],
            options={
                'verbose_name': 'orderComment',
                'verbose_name_plural': 'orderComments',
            },
        ),
    ]
