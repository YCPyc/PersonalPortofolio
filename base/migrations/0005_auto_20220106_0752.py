# Generated by Django 3.2.8 on 2022-01-06 07:52

import ckeditor_uploader.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20211229_0438'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('subject', models.CharField(max_length=200, null=True)),
                ('body', models.TextField()),
                ('is_read', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
