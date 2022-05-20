from django.db import models

# Create your models here.
class QuoteModel(models.Model):
    name = models.CharField(verbose_name="name",max_length=150)
    email = models.EmailField(verbose_name="email",max_length=150)
    tel = models.CharField(verbose_name="tel",max_length=30)
    company_name = models.CharField(verbose_name="company_name",max_length=100)
    mc = models.CharField(verbose_name="mc#",max_length=100)
    dry_van = models.BooleanField(verbose_name="dry_van", blank=True)
    reefer = models.BooleanField(verbose_name="reefer", blank=True)
    flat_bed = models.BooleanField(verbose_name="flat_bed", blank=True)
    message = models.TextField(verbose_name="message")
    need_driver_assistence = models.BooleanField(verbose_name="need_driver_assistence",blank=True)

    def __str__(self):
        return self.name

class Drivers(models.Model):

    WHICH_POSITION = (
                        ('solo_driver','Solo Driver'),
                        ('team_driver','Team driver'),
                        ('owner_operator','Owner operator'),
                            )
    first_name             =  models.CharField(verbose_name="first name", max_length=150)
    last_name              =  models.CharField(verbose_name="last name", max_length=150,blank=True)
    email                  =  models.EmailField(verbose_name="email",max_length=100)
    phone                  =  models.BigIntegerField(verbose_name="phone number")
    driver_license         =  models.IntegerField(verbose_name="driver license")
    state                  =  models.CharField(verbose_name="state",max_length=50)
    driving_information    =  models.TextField(verbose_name="driving information")
    how_many_years         =  models.TextField(verbose_name="how_many_years")
    # previus_employer       =  models.IntegerField(verbose_name="driver license")
    previus_employer       =  models.CharField(verbose_name="driver license", max_length=500)
    which_position         =  models.CharField(verbose_name="Which position are you interested in?",max_length=50,choices=WHICH_POSITION )

    def __str__(self):
        return self.first_name