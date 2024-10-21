# from django.contrib import admin
# from .models import Task, Priority
#
#
# class TaskAdmin(admin.ModelAdmin):
#     list_display = ('name', 'completed', 'due_date', 'created_at', 'profile', 'priority')
#     list_filter = ('completed', 'priority', 'profile')
#     search_fields = ('name', 'description')
#     ordering = ('-created_at',)
#     list_editable = ('completed', 'priority')
#
#     def get_priority_display(self, obj):
#         return obj.priority.capitalize()
#
#
# admin.site.register(Task, TaskAdmin)
