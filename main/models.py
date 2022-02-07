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