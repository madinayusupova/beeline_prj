from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number')
    list_filter = ('name', 'phone_number')
    search_fields = ('name', 'phone_number')
    ordering = ('name', 'phone_number')

# Register your models here.
