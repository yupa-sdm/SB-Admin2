# Generated by Django 3.2.5 on 2021-09-02 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_rename_help_line_article_head_line'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Reporter',
        ),
    ]