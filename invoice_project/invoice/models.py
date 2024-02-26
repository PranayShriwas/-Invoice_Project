from django.db import models

class UserDetails(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    gst_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name  # Or any other field that you want to display as the string representation

class InvoiceDetails(models.Model):
    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    service = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Invoice for {self.user.name}"
