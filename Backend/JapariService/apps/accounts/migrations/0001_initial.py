# Generated by Django 4.2.2 on 2023-07-05 07:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestEntry',
            fields=[
                ('id', models.SmallAutoField(editable=False, primary_key=True, serialize=False)),
                ('text', models.CharField(error_messages={'blank': 'the test neads a text'}, max_length=32, unique_for_date='pub_date', verbose_name='text')),
                ('pub_date', models.DateTimeField(blank=True, default=django.utils.timezone.localtime, editable=False, verbose_name='date published')),
            ],
            options={
                'verbose_name': 'test accounts-app entry',
                'verbose_name_plural': 'test accounts-app entries',
                'db_table': 'test_accounts',
                'ordering': ['pub_date'],
                'get_latest_by': ['pub_date'],
            },
        ),
    ]
