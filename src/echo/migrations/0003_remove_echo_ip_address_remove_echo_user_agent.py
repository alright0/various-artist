# Generated by Django 4.1.2 on 2022-10-09 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("echo", "0002_alter_echo_options_echo_ip_address_echo_user_agent"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="echo",
            name="ip_address",
        ),
        migrations.RemoveField(
            model_name="echo",
            name="user_agent",
        ),
    ]
