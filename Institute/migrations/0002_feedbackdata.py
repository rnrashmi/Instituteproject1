# Generated by Django 2.2.7 on 2020-01-26 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Institute', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('date', models.DateTimeField(max_length=100)),
                ('feedback', models.CharField(max_length=100)),
            ],
        ),
    ]