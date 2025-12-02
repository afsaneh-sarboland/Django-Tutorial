from django.contrib import admin
from .models import Contact



# Register your models here.
# admin.site.register(Contact)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
    list_per_page = 20 
    date_hierarchy = 'created_at'