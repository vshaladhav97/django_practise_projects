from django.db.models.signals import post_save
from django.dispatch import receiver
from projects.models import Project
from access_management.utils import generate_groups_and_permission
from django.contrib.contenttypes.models import ContentType
from project_calendars.models import CalendarBriefMapping
from access_management.constants.project_constants import *
from django.contrib.auth.models import Group


@receiver(post_save, sender=Project)
def create_groups_for_project(sender, instance, **kwargs):
    if kwargs['created']:
        try:
            content_type = ContentType.objects.get(
                model=instance._meta.model_name)
            generate_groups_and_permission(instance._meta.model_name,
                                            str(instance.id), content_type)

            super_group = Group.objects.get(
                name=str(instance.id) + '-' + PROJECT_SUPER_GROUP)
            view_group = Group.objects.get(
                name=str(instance.id) + '-' + PROJECT_VIEW_ONLY_GROUP)
            instance.editor.user_id.groups.add(super_group)
            instance.client.user_id.groups.add(view_group)

        except Exception as e:
            raise e
    else:
        print("Object not created yet.")
