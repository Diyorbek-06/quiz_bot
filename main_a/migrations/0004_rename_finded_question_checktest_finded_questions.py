# Generated by Django 5.2 on 2025-06-22 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_a', '0003_checkquestion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checktest',
            old_name='finded_question',
            new_name='finded_questions',
        ),
    ]
