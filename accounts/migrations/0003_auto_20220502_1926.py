# Generated by Django 3.1.3 on 2022-05-02 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_truckcustomer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='truckcustomer',
            name='user',
        ),
        migrations.AddField(
            model_name='truckcustomer',
            name='companyName',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.company'),
        ),
        migrations.AlterField(
            model_name='order',
            name='companyName',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.truckcustomer'),
        ),
    ]
