from django.contrib import admin

from . import models

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(models.Projects, ProjectsAdmin)