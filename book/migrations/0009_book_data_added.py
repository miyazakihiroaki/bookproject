# Generated by Django 3.2 on 2022-07-12 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_remove_book_data_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='data_added',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=False,
        ),
    ]
