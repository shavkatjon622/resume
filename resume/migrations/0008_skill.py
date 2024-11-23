# Generated by Django 5.1.3 on 2024-11-19 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0007_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('KS', 'Key skills'), ('AS', 'Additional skills')], max_length=2)),
            ],
        ),
    ]