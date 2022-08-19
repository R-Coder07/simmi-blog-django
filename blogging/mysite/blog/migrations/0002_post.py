# Generated by Django 4.1 on 2022-08-19 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField(max_length=30)),
                ('date_posted', models.DateField(auto_now_add=True)),
                ('description', models.TextField(max_length=30)),
                ('image_file', models.FileField(default='', upload_to='blog/pics')),
            ],
        ),
    ]
