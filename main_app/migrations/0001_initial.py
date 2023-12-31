# Generated by Django 3.2.12 on 2023-09-14 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Finch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species', models.CharField(max_length=150)),
                ('population', models.IntegerField()),
                ('population_trend', models.CharField(choices=[('INC', 'Increading'), ('DEC', 'Decreasing'), ('UNK', 'Unknown')], default='UNK', max_length=3)),
            ],
        ),
    ]
