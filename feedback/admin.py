from django.contrib import admin
from .models import Complain,Suggestion

# Register your models here.
admin.site.register(Suggestion)

@admin.register(Complain)
class ComplainAdmin(admin.ModelAdmin):
    '''Admin View for Complain'''

    list_display = ('department', 'complain', 'add_time')
    list_filter = ('department',)
    search_fields = ('department',)
    date_hierarchy = 'add_time'
    ordering = ('-department',)
