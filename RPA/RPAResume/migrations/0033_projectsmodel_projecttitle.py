# Generated by Django 4.1.7 on 2023-04-17 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RPAResume', '0032_alter_commentsmodel_comments1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectsmodel',
            name='ProjectTitle',
            field=models.CharField(default=None, max_length=254),
        ),
    ]
