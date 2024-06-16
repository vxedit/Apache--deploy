from django.contrib import admin
from miapp.models import Item

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name','description', 'created_at')
    search_fields = ('name',)

admin.site.register(Item, ItemAdmin)