from django.contrib import admin
from .models import Profile, Language, Project, Rating

# Register your models here.
admin.site.register(Profile)
admin.site.register(Language)
admin.site.register(Project)
admin.site.register(Rgating)