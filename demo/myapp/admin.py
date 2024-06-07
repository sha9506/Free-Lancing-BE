from django.contrib import admin
from myapp.models import user , jobs, payment

# Register your models here.
@admin.register(user, jobs, payment)
class PersonAdmin(admin.ModelAdmin):
    pass