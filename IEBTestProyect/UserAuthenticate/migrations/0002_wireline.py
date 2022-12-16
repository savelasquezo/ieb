# Generated by Django 4.1.3 on 2022-12-14 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserAuthenticate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wireline',
            fields=[
                ('cod_wireline', models.BigAutoField(primary_key=True, serialize=False)),
                ('material', models.CharField(max_length=128)),
                ('ampacity', models.IntegerField()),
                ('new_voltage', models.IntegerField()),
                ('new_thickness', models.IntegerField()),
                ('new_diameter', models.IntegerField()),
                ('new_current', models.IntegerField()),
            ],
        ),
    ]