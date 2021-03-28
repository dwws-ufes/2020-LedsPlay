# Generated by Django 3.1.7 on 2021-03-28 02:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='Nome', max_length=120)),
                ('sexo', models.CharField(default='M or F', max_length=1)),
                ('email', models.EmailField(default='Email', max_length=120)),
                ('nascimento', models.DateField(default=datetime.date.today)),
                ('password', models.CharField(default='password', max_length=128)),
            ],
        ),
    ]
