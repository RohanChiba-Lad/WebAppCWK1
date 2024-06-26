# Generated by Django 5.0.2 on 2024-03-20 18:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NewsStory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=64)),
                ('category', models.CharField(choices=[('pol', 'Politics'), ('art', 'Art'), ('tech', 'Technology'), ('trivia', 'Trivia')], max_length=10)),
                ('region', models.CharField(choices=[('uk', 'UK'), ('eu', 'Europe'), ('w', 'World')], max_length=5)),
                ('story_date', models.DateTimeField(auto_now_add=True)),
                ('details', models.CharField(max_length=128)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.author')),
            ],
        ),
    ]
