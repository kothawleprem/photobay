# Generated by Django 3.0.2 on 2020-05-20 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sn0', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
