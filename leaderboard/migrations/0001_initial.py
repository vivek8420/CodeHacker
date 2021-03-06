# Generated by Django 2.1.7 on 2019-03-20 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='point_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=20)),
                ('challenge_code', models.CharField(max_length=10)),
                ('maxscore', models.IntegerField(default=0)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='problem_score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('challenge_code', models.CharField(max_length=20)),
                ('user_id', models.CharField(max_length=20)),
                ('problem_code', models.CharField(max_length=10)),
                ('score', models.IntegerField(default=0)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
