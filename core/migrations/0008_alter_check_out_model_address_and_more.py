# Generated by Django 5.0.7 on 2024-08-16 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_check_out_model_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check_out_model',
            name='address',
            field=models.TextField(blank=True, max_length=35, null=True),
        ),
        migrations.AlterField(
            model_name='check_out_model',
            name='post_code',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='check_out_model',
            name='state',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
