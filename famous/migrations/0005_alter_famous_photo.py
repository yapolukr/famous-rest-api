# Generated by Django 4.1.1 on 2022-09-12 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('famous', '0004_alter_category_options_alter_famous_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='famous',
            name='photo',
            field=models.ImageField(null=True, upload_to='photos/'),
        ),
    ]