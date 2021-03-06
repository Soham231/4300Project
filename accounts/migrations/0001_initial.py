# Generated by Django 3.1.3 on 2022-05-02 05:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('email', models.CharField(max_length=30, null=True)),
                ('phone', models.CharField(max_length=30, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='profile.png', null=True, upload_to='')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driverName', models.CharField(max_length=30, null=True)),
                ('driverLocation', models.CharField(max_length=30, null=True)),
                ('driverStatus', models.CharField(choices=[('Ready', 'Ready'), ('Driving', 'Driving'), ('Off', 'Off')], max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TruckLoad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loadName', models.CharField(max_length=30, null=True)),
                ('loadPrice', models.FloatField(null=True)),
                ('loadWeight', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderID', models.CharField(max_length=10, null=True)),
                ('origin', models.CharField(max_length=50, null=True)),
                ('destination', models.CharField(max_length=50, null=True)),
                ('dateLeft', models.DateField()),
                ('dateArrived', models.DateField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Shipping', 'Shipping'), ('Arrived', 'Arrived')], max_length=50, null=True)),
                ('companyName', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.company')),
                ('load', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.truckload')),
                ('trucker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.driver')),
            ],
        ),
    ]
