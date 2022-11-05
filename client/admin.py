from django.contrib import admin
from .models import IchkiMijoz, TashqiMijoz


@admin.register(IchkiMijoz)
class InternalClientAdmin(admin.ModelAdmin):
    list_display = ("name", "surname", "phone_number", "address", "upload_date", "order")


@admin.register(TashqiMijoz)
class InternalClientAdmin(admin.ModelAdmin):
    list_display = ("name", "surname", "phone_number", "address", "upload_date", "order")
