from django.contrib.auth.models import Permission, User
from django.db import models
from calendarium.models import Identity_Information

class bill(models.Model):
    identity = models.ForeignKey(Identity_Information, on_delete=models.CASCADE)
    recieved_from = models.CharField(max_length=50)
    date = models.DateField()
    sum_in_words = models.CharField(max_length=50)
    sum = models.DecimalField(decimal_places=2, max_digits=38)
    total_sales_vat_inclusive = models.DecimalField(decimal_places=2, max_digits=38)
    less_vat = models.DecimalField(decimal_places=2, max_digits=38)
    total = models.DecimalField(decimal_places=2, max_digits=38)
    less_sc_pwd_disc = models.DecimalField(decimal_places=2, max_digits=38)
    less_withholding_tax = models.DecimalField(decimal_places=2, max_digits=38)
    amount_due = models.DecimalField(decimal_places=2, max_digits=38)
    vatable_sales = models.DecimalField(decimal_places=2, max_digits=38)
    vat_exempt_sales = models.DecimalField(decimal_places=2, max_digits=38)
    vat_zero_rated_sales = models.DecimalField(decimal_places=2, max_digits=38)
    vat_amount = models.DecimalField(decimal_places=2, max_digits=38)
    total_sales = models.DecimalField(decimal_places=2, max_digits=38)
    is_full = models.BooleanField(default=True)

    def __str__(self):
        return self.recieved_from


