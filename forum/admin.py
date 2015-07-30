from django.contrib import admin

# Register your models here.

from .models import Thread
admin.site.register(Thread)
from .models import Comment
admin.site.register(Comment)

