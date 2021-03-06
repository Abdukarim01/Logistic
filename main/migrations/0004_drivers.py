# Generated by Django 4.0.1 on 2022-02-20 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_quotemodel_tel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drivers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(max_length=100, verbose_name='email')),
                ('phone', models.IntegerField(verbose_name='phone number')),
                ('driver_license', models.IntegerField(verbose_name='driver license')),
                ('state', models.CharField(max_length=50, verbose_name='state')),
                ('driving_information', models.TextField(verbose_name='driving information')),
                ('how_many_years', models.TextField(verbose_name='how_many_years')),
                ('previus_employer', models.CharField(choices=[('previus_employer', 'Previus employer'), ('usdot_number', 'USDOT number')], max_length=50, verbose_name='Previus employer')),
                ('which_position', models.CharField(choices=[('solo_driver', 'Solo Driver'), ('team_driver', 'Team driver'), ('owner_operator', 'Owner operator')], max_length=50, verbose_name='Which position are you interested in?')),
            ],
        ),
    ]
