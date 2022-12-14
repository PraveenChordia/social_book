# Generated by Django 4.1.2 on 2022-10-17 13:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("social_book_app", "0005_alter_userdetails_last_login"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userdetails",
            name="last_login",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Last Login",
            ),
            preserve_default=False,
        ),
    ]
