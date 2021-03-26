from django.contrib import admin
from .models import Feedback
from django.contrib.admin import ModelAdmin
from .forms import FeedbackForm, FeedbackAddForm
from .actions import mark_feedback_as_read

class FeedbackAdmin(ModelAdmin):
  form = FeedbackForm
  list_display = ('name', 'category', 'email', 'subject', 'is_read',)
  list_editable = ('subject', 'is_read',)
  search_fields = ('name', 'category', 'email', 'subject',)
  actions_on_bottom = True
  save_on_top = True
  actions = [mark_feedback_as_read]

  def get_form(self, request, obj=None, **kwargs):

    if (obj is None):
      return FeedbackAddForm
    else: return super(FeedbackAdmin, self).get_form(request, obj, **kwargs)


admin.site.register(Feedback, FeedbackAdmin)
