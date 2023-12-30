# Generated by Django 4.0.4 on 2022-06-03 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geeks', '0003_geeksmodel_arrival'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentsModel1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=30)),
                ('zipcode', models.CharField(max_length=10)),
                ('nameoncard', models.CharField(max_length=20)),
                ('cardnumber', models.CharField(max_length=16)),
                ('expmonth', models.CharField(max_length=20)),
                ('expyear', models.CharField(max_length=4)),
                ('cvv', models.CharField(max_length=3)),
            ],
        ),
    ]
