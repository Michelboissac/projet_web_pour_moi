# Generated by Django 5.0 on 2024-01-23 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangalib', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_genome', models.CharField(max_length=32, unique=True)),
                ('sequence', models.TextField()),
            ],
        ),
    ]
