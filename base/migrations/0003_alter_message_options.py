# Generated by Django 4.1 on 2022-08-10 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_room_options_room_participants'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-updated', '-created']},
        ),
    ]
