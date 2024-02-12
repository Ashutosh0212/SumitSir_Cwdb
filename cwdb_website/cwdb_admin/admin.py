from django.contrib import admin
from .models import Index_Notification

class IndexNotificationAdmin(admin.ModelAdmin):
    list_display = ('message', 'created_at', 'is_read')
    readonly_fields = ('created_at', 'is_read')  # Make created_at and is_read readonly
    fields = ('message',)  # Only allow admin to edit the message field

    def save_model(self, request, obj, form, change):
        """Automatically set created_at and is_read fields"""
        if not obj.pk:  # If creating a new object
            obj.is_read = False  # Mark as unread
        obj.save()

admin.site.register(Index_Notification, IndexNotificationAdmin)
