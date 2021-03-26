def mark_feedback_as_read(modeladmin, request, queryset):
  for employeefeedback in queryset:
    employeefeedback.is_read = True
    employeefeedback.save()
  modeladmin.message_user(request, '%s successfully marked as read' % len(queryset))

mark_feedback_as_read.short_description = 'Mark selected feedback as read'
