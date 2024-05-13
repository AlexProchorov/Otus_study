# Generated by Django 5.0.3 on 2024-05-09 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=255, verbose_name='UserName')),
                ('SumCount', models.IntegerField(blank=True, null=True, verbose_name='Sum')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('Message', models.CharField(max_length=255, verbose_name='Message')),
            ],
        ),
    ]
