# Generated by Django 2.0.2 on 2020-10-11 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201011_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='publication_date',
            field=models.DateTimeField(),
        ),
    ]
