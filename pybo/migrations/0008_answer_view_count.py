# Generated by Django 3.1.3 on 2022-06-19 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0007_questioncount'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='view_count',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]