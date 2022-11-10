from django.contrib import admin
from .models import Page
# Register your models here.

class PageAdmin(admin.ModelAdmin):
    list_filter = ('visible',)
    list_display = ('title', 'visible', 'created_at')

admin.site.register(Page, PageAdmin)

admin.site.site_header = "Proyecto Con Django"
admin.site.site_title = "Proyecto Con Django"
admin.site.index_title = "Panel De Gestion"
