from django.contrib import admin
from home.models import Text


class TextAdmin(admin.ModelAdmin):
    list_display = ['text', 'lang']


admin.site.register(Text, TextAdmin)
