# Generated by Django 2.1.1 on 2018-09-28 07:43

from django.db import migrations, models
import livegene.apps.livegene.validators


class Migration(migrations.Migration):

    dependencies = [
        ('livegene', '0012_auto_20180925_1355'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=30)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, validators=[livegene.apps.livegene.validators.validate_lowercase])),
                ('phone', models.CharField(blank=True, max_length=30)),
            ],
            options={
                'verbose_name_plural': 'contact people',
                'ordering': ('last_name', 'first_name'),
            },
        ),
        migrations.RemoveField(
            model_name='expenditure',
            name='project',
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'ordering': ('country',), 'verbose_name_plural': 'countries'},
        ),
        migrations.AlterModelOptions(
            name='partnershiproletype',
            options={'ordering': ('pk',)},
        ),
        migrations.DeleteModel(
            name='Expenditure',
        ),
    ]