from django.contrib import admin
from .models import MyModel

class MyModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone')
    list_filter = ('category', 'created_at')
    search_fields = ('name', 'email', 'phone')
    ordering = ('-created_at',)
    # form = MyModelForm
    fieldsets = (
        ('Main Information', {
            'fields': ('name', 'email', 'phone')
        }),
        ('Additional Information', {
            'fields': ('category', 'description')
        }),
    )
    readonly_fields = ('created_at',)
    
    def save_model(self, request, obj, form, change):
        # Custom model saving behavior
        super().save_model(request, obj, form, change)


