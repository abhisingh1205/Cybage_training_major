# Generated by Django 2.2.17 on 2020-11-23 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0002_auto_20201123_0421'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestString',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('string', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='entry',
            name='test_string',
        ),
        migrations.AddField(
            model_name='entry',
            name='test_strings',
            field=models.ManyToManyField(to='entries.TestString'),
        ),
    ]
