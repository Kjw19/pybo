# Generated by Django 3.1.3 on 2022-06-22 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0012_category_has_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='view_count',
        ),
    ]
