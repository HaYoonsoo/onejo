from django.contrib import admin
from .models import Profile, Pig, Schedule

# Register your models here.
admin.site.register(Profile)
admin.site.register(Pig)
admin.site.register(Schedule)