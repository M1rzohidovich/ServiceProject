from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import InternalBlog,  ExternalBlog,  WorkerContact, Announcement


admin.site.register((InternalBlog, ExternalBlog, WorkerContact, Announcement))