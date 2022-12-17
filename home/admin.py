from django.contrib import admin

# Register your models here.
from home.models import Settings, ContactFormMessage


class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message', 'note', 'status']
    list_filter = ['status', 'subject']


admin.site.register(ContactFormMessage, ContactFormMessageAdmin)
admin.site.register(Settings)
