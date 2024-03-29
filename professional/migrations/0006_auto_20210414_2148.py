# Generated by Django 3.2 on 2021-04-15 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('professional', '0005_alter_profissional_competencia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profissional',
            name='avaliacao',
        ),
        migrations.AddField(
            model_name='avaliacao',
            name='profissional',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='professional.profissional'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='nota',
            field=models.IntegerField(null=True),
        ),
    ]
