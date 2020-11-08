from django.contrib import admin
from application.models import appointment, user

# Register your models here.
admin.site.register(user)
admin.site.register(appointment)
