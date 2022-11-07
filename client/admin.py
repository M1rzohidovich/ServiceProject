from django.contrib import admin
from .models import IchkiMijoz, TashqiMijoz


@admin.register(IchkiMijoz)
class InternalClientAdmin(admin.ModelAdmin):
    list_display = ("name", "surname", "phone_number", "address", "comment", "cleaning_date", "upload_date", "order")


@admin.register(TashqiMijoz)
class InternalClientAdmin(admin.ModelAdmin):
    list_display = ("name", "surname", "phone_number", "address", "comment", "cleaning_date", "upload_date", "order")
