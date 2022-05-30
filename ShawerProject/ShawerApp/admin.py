from django.contrib import admin
from .models import counselor, comment
# Register your models here.

class counselorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'start_date','expertise_field')
    list_filter = ('expertise_field',)
admin.site.register(counselor, counselorAdmin)
admin.site.register(comment)