# myapp/admin.py

from django.contrib import admin
from .models import ContactMessage
from .models import Upload

admin.site.register(ContactMessage)
admin.site.register(Upload)