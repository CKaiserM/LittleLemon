# Generated by Django 5.0 on 2024-01-14 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('reservation_date', models.DateField()),
                ('no_of_guests', models.SmallIntegerField(default=6)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('price', models.DecimalField(db_index=True, decimal_places=2, max_digits=6)),
                ('inventory', models.SmallIntegerField(default=5)),
            ],
        ),
    ]
