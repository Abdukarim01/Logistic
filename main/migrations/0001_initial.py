# Generated by Django 4.0.1 on 2022-02-04 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuoteModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='name')),
                ('email', models.EmailField(max_length=150, verbose_name='email')),
                ('tel', models.IntegerField(verbose_name='tel')),
                ('company_name', models.CharField(max_length=100, verbose_name='company_name')),
                ('mc', models.CharField(max_length=100, verbose_name='mc#')),
                ('dry_van', models.BooleanField(blank=True, verbose_name='dry_van')),
                ('reefer', models.BooleanField(blank=True, verbose_name='reefer')),
                ('flat_bed', models.BooleanField(blank=True, verbose_name='flat_bed')),
                ('message', models.TextField(verbose_name='message')),
                ('need_driver_assistence', models.BooleanField(blank=True, verbose_name='need_driver_assistence')),
            ],
        ),
    ]