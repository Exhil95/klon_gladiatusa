# Generated by Django 5.1.6 on 2025-04-01 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lokacje', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enemy',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='enemy',
            name='name',
            field=models.CharField(default='test_object', max_length=25),
        ),
    ]
