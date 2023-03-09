from django.contrib import admin
from . models import Category, Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_name', 'email', 'created_at', 'phone', 'active','pic')
    list_filter = ('name', 'last_name', 'email')
    list_per_page = 10
    search_fields = ('name', 'last_name')
    list_editable = ('phone', 'active')

admin.site.register(Category)
admin.site.register(Contact, ContactAdmin)