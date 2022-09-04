from django.db import models

# Create your models here.
class Clients(models.Model):
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    email = models.EmailField(unique=True)
    id_number = models.CharField(max_length=30, blank=False)
    is_verified = models.BooleanField(default=False)
    address = models.CharField(max_length=30, blank=False)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    proof_of_address = models.FileField(upload_to='proof_of_address', blank=True, null=True)
    proof_of_id = models.FileField(upload_to='proof_of_id', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Loan(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    contract = models.FileField(upload_to='contracts', blank=True, null=True)
    repayment_date = models.DateField(null=True,blank=True)
    is_approved = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_paid = models.BooleanField(default=False)
    is_overdue = models.BooleanField(default=False)
    is_defaulted = models.BooleanField(default=False)
    date_requested = models.DateTimeField(auto_now_add=True)
    date_approved = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return f"{self.client} {self.amount}"

class InterestRate(models.Model):
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.rate}"

