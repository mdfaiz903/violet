from django.db import models

# Create your models here.
class Coupon(models.Model):
    code = models.CharField(max_length=50,unique=True)
    discount = models.PositiveBigIntegerField(help_text="Discount in percentage")
    active = models.BooleanField(default=True)
    active_date = models.DateField()
    expiry_date = models.DateField()
    required_amount_to_use_coupon= models.PositiveBigIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self)->str:
        return self.code
    