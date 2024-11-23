# Generated by Django 5.1.3 on 2024-11-19 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_alter_language_degree'),
    ]

    operations = [
        migrations.CreateModel(
            name='LatestProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='project/')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('url', models.URLField()),
            ],
        ),
    ]