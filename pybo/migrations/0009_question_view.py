# Generated by Django 3.1.3 on 2022-06-20 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0008_answer_view_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='view',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
