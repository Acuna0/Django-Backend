# Generated by Django 5.0.3 on 2024-03-18 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techexercise', '0005_remove_user_is_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
    ]