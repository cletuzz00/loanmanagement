from django.contrib import admin

# Register your models here.
from users.models import User

@admin.register(User)
class UniversalAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]

    