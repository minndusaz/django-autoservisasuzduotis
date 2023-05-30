# Generated by Django 4.2.1 on 2023-05-30 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AutomobilioModelis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car', models.CharField(max_length=100, verbose_name='car')),
                ('car_model', models.CharField(max_length=100, verbose_name='model')),
            ],
            options={
                'verbose_name': 'automobilioModelis',
                'verbose_name_plural': 'automobilioModeliai',
            },
        ),
        migrations.CreateModel(
            name='Automobilis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_number', models.CharField(default=None, max_length=10, verbose_name='car_number')),
                ('vin_number', models.CharField(default=None, max_length=17, verbose_name='vin_number')),
                ('client_name', models.CharField(db_index=True, max_length=50, verbose_name='client_name')),
                ('client_surname', models.CharField(db_index=True, max_length=50, verbose_name='client_surname')),
                ('car_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='automobiliai', to='autoservisasinfo.automobiliomodelis', verbose_name='automobilio modelis')),
            ],
            options={
                'verbose_name': 'automobilis',
                'verbose_name_plural': 'automobiliai',
                'ordering': ['client_name', 'client_surname'],
            },
        ),
        migrations.CreateModel(
            name='Paslauga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('price', models.FloatField(verbose_name='price')),
            ],
            options={
                'verbose_name': 'paslauga',
                'verbose_name_plural': 'paslaugos',
            },
        ),
        migrations.CreateModel(
            name='UzsakymoEilute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=None, verbose_name='count')),
                ('total_price', models.FloatField(default=None, verbose_name='total_price')),
                ('paslauga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uzsakymoeilutes', to='autoservisasinfo.paslauga', verbose_name='')),
            ],
            options={
                'verbose_name': 'uzsakymoEilute',
                'verbose_name_plural': 'uzsakymoEilutes',
            },
        ),
        migrations.CreateModel(
            name='Uzsakymas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateField(verbose_name='order_date')),
                ('price', models.FloatField(verbose_name='price')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uzsakymai', to='autoservisasinfo.automobilis', verbose_name='automobilis')),
                ('order_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uzsakymai', to='autoservisasinfo.uzsakymoeilute', verbose_name='')),
            ],
            options={
                'verbose_name': 'uzsakymas',
                'verbose_name_plural': 'uzsakymai',
            },
        ),
    ]