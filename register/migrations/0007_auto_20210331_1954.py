# Generated by Django 3.1.7 on 2021-03-31 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0006_ordem_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordem',
            name='competencia',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='register.competencia'),
        ),
        migrations.AddField(
            model_name='ordem',
            name='costumer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='register.pessoa'),
        ),
    ]
