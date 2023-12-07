# Generated by Django 4.2.5 on 2023-12-06 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_uid', models.TextField(unique=True)),
                ('user_username', models.TextField(default=None, null=True)),
                ('user_name', models.TextField()),
                ('user_email', models.TextField()),
                ('user_pfp', models.TextField()),
                ('user_quizzes_hosted', models.IntegerField(default=0)),
                ('user_quizzes_joined', models.IntegerField(default=0)),
            ],
        ),
    ]
