# Generated by Django 3.2.5 on 2021-07-10 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_rename_post_comment_posts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='posts',
            new_name='post',
        ),
    ]
