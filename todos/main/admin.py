from django.contrib import admin
from main.models import Todo
# Register your models here.

class TodoAdmin(admin.ModelAdmin):

    list_display = ['id','title', 'due_date', 'done']
    list_filter = ['due_date', 'done']
    ordering = ('-due_date',)

admin.site.register(Todo, TodoAdmin)
