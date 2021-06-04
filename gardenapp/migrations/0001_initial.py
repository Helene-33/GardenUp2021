# Generated by Django 3.2.3 on 2021-06-03 17:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plantname', models.CharField(max_length=255)),
                ('dateentered', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('planturl', models.URLField()),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'plants',
                'db_table': 'plant',
            },
        ),
        migrations.CreateModel(
            name='PlantType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typename', models.CharField(max_length=255)),
                ('typedescription', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'planttypes',
                'db_table': 'planttype',
            },
        ),
        migrations.CreateModel(
            name='Tips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('tipdate', models.DateField()),
                ('tiptext', models.TextField()),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gardenapp.plant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tips',
            },
        ),
        migrations.AddField(
            model_name='plant',
            name='planttype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='gardenapp.planttype'),
        ),
        migrations.AddField(
            model_name='plant',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]