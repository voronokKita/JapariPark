# Generated by Django 4.2.2 on 2023-06-21 15:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ListEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_text', models.CharField(max_length=200, verbose_name='text')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='date published')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='list_entries', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'List entry',
                'verbose_name_plural': 'List entries',
                'ordering': ['-pub_date'],
            },
        ),
    ]