from django.contrib import admin

# Register your models here.
from loans.models import Loan, Clients, InterestRate

@admin.register(Loan,Clients,InterestRate)
class UniversalAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]

    