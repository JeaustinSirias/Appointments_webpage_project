from django.contrib import admin
from application.models import appointment, user
from application.forms import SignUpForm

# Register your models here.
admin.site.register(user)
admin.site.register(appointment)
#admin.site.register(SignUpForm)
