# Generated by Django 2.1.4 on 2019-02-13 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0006_forum_post_p_categorie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forum_post',
            name='p_categorie',
        ),
    ]