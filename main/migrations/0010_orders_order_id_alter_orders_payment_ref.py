# Generated by Django 4.1.6 on 2023-04-01 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_review_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='order_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='orders',
            name='payment_ref',
            field=models.CharField(default='', max_length=25),
        ),
    ]