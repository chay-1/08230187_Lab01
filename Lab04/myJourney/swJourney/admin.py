from django.contrib import admin
from .models import LearningEntry, AboutMe

@admin.register(LearningEntry)
class LearningEntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title', 'content')

@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'roll_number')
