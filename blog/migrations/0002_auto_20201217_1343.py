# Generated by Django 3.1.4 on 2020-12-17 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='Con_heading0',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='Con_heading1',
            field=models.CharField(default='', max_length=20000),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='Con_sub_heading',
            field=models.CharField(default='', max_length=30000),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='category',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='sub_category',
            field=models.CharField(default='', max_length=100),
        ),
    ]
