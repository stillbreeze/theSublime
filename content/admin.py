from django.contrib import admin
from content.models import *
# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(SubComment)