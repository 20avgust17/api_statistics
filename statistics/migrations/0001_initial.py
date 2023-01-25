# Generated by Django 4.1.5 on 2023-01-03 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True, verbose_name='Время создания')),
                ('views', models.IntegerField(max_length=10, verbose_name='Количество просмотров')),
                ('clicks', models.IntegerField(max_length=10, verbose_name='Количество кликов')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=999, verbose_name='Цена')),
            ],
        ),
    ]
