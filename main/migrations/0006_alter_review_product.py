# Generated by Django 4.1.6 on 2023-03-16 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_review_email_review_name_alter_review_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='product',
            field=models.CharField(default='', max_length=100),
        ),
    ]
