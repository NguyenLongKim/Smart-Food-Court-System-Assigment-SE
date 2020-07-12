# Generated by Django 3.0.8 on 2020-07-12 12:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cook',
            options={'verbose_name': 'Cook', 'verbose_name_plural': 'Cooks'},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'Customer', 'verbose_name_plural': 'Customers'},
        ),
        migrations.AlterModelOptions(
            name='manager',
            options={'verbose_name': 'Manager', 'verbose_name_plural': 'Managers'},
        ),
        migrations.AlterModelOptions(
            name='vendorowner',
            options={'verbose_name': 'VendorOwner', 'verbose_name_plural': 'VendorOwners'},
        ),
        migrations.RemoveField(
            model_name='user',
            name='type_account',
        ),
        migrations.AddField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Customer'), (2, 'VendorOwner'), (3, 'Cook'), (4, 'Manager')], default=4),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='email address'),
        ),
    ]
