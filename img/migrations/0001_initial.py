# Generated by Django 3.1.4 on 2021-02-07 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Github',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('githubuser', models.CharField(max_length=1000)),
                ('imagelink', models.CharField(max_length=10000)),
                ('username', models.CharField(max_length=1000)),
            ],
        ),
    ]