# Generated by Django 3.2.5 on 2021-07-11 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0003_auto_20210711_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizzes',
            name='right_answers',
            field=models.TextField(),
        ),
    ]
