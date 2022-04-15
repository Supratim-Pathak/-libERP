# Generated by Django 4.0.2 on 2022-04-14 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='books_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.IntegerField()),
                ('book_name', models.CharField(max_length=150)),
                ('isbn_no', models.CharField(max_length=100)),
                ('current_stock', models.IntegerField(null=b'I01\n')),
            ],
        ),
    ]
