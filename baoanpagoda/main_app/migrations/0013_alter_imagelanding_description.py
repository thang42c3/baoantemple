# Generated by Django 4.2.5 on 2023-10-08 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_menu_description_menu_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagelanding',
            name='description',
            field=models.TextField(blank=True, help_text='You can use HTML tags for styling.', null=True),
        ),
    ]
