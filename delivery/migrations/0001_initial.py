# Generated by Django 2.0.1 on 2018-10-22 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=20)),
                ('address', models.TextField(default=None, max_length=200)),
                ('contact_number', models.CharField(default=None, max_length=10)),
                ('date_of_birth', models.DateField(null=True)),
                ('grand_total', models.CharField(default=None, max_length=20)),
            ],
        ),
    ]