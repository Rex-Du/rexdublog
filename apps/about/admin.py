from django.contrib import admin

from .models import Experiences


class ExperiencesAdmin(admin.ModelAdmin):
    list_display = ['content', 'add_time']


# Register your models here.
admin.site.register(Experiences, ExperiencesAdmin)
