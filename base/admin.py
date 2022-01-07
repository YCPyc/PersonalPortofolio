from django.contrib import admin
from .models import Project, Skills, tags, Message
# Register your models here.

admin.site.register(Project)
admin.site.register(Skills)
admin.site.register(tags)
admin.site.register(Message)