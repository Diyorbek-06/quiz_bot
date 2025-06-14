# Generated by Django 5.2 on 2025-05-29 17:47

import django.db.models.deletion
import django.utils.timezone
import main_a.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('max_attemps', models.PositiveIntegerField()),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_date', models.DateTimeField(default=main_a.models.get_default_end_date)),
                ('pass_percentage', models.PositiveIntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_a.category')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('a', models.CharField(max_length=150)),
                ('b', models.CharField(max_length=150)),
                ('c', models.CharField(max_length=150)),
                ('d', models.CharField(max_length=150)),
                ('true_answer', models.CharField(help_text='E.x: a', max_length=150)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_a.test')),
            ],
        ),
    ]
