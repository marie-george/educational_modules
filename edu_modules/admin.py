from django.contrib import admin

from edu_modules.models import EduModule


@admin.register(EduModule)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'owner')
