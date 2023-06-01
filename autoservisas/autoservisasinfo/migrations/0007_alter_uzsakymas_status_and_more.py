# Generated by Django 4.2.1 on 2023-05-31 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoservisasinfo', '0006_alter_uzsakymas_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uzsakymas',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Confirmed'), (1, 'In Progress'), (2, 'Finished'), (3, 'Canceled')], db_index=True, default=0, verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='uzsakymoeilute',
            name='total_price',
            field=models.FloatField(default=0, verbose_name='total_price'),
        ),
    ]