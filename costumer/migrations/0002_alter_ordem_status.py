# Generated by Django 3.2 on 2021-04-09 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costumer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordem',
            name='status',
            field=models.CharField(choices=[('STAND BY', 'STAND BY'), ('EM OPERAÇÃO', 'EM OPERAÇÃO'), ('FINALIZADO', 'FINALIZADO')], max_length=120, null=True),
        ),
    ]
