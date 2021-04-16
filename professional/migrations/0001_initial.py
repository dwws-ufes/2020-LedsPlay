# Generated by Django 3.1.7 on 2021-04-16 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, null=True)),
                ('category', models.CharField(choices=[('CATEGORY 1', 'CATEGORY 1'), ('CATEGORY 2', 'CATEGORY 2'), ('CATEGORY 3', 'CATEGORY 3')], max_length=120, null=True)),
                ('description', models.CharField(max_length=120, null=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
