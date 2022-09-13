# Generated by Django 4.1.1 on 2022-09-11 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('rollno', models.IntegerField(max_length=50)),
                ('course', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
    ]