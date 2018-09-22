# Generated by Django 2.1.1 on 2018-09-21 14:14

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('livegene', '0002_auto_20180921_1407'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'ordering': ('country',)},
        ),
        migrations.RemoveField(
            model_name='country',
            name='alpha2_code',
        ),
        migrations.RemoveField(
            model_name='country',
            name='alpha3_code',
        ),
        migrations.RemoveField(
            model_name='country',
            name='name',
        ),
        migrations.AddField(
            model_name='country',
            name='country',
            field=django_countries.fields.CountryField(default='', max_length=2),
            preserve_default=False,
        ),
    ]