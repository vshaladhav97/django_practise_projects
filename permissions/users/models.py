from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.translation import gettext as _
# User classnew_group, created = Group.objects.get_or_create(name ='new_group')


class User(AbstractUser):

    # Define the extra fields
    # related to User here
    first_name = models.CharField(_('First Name of User'), blank=True, max_length=20)
    last_name = models.CharField(_('Last Name of User'), blank=True, max_length=20)

# More User fields according to need

    # define the custom permissions
    # related to User.
    class Meta:

        permissions = (
            ("can_go_in_non_ac_bus", "To provide non-AC Bus facility"),
            ("can_go_in_ac_bus", "To provide AC-Bus facility"),
            ("can_stay_ac-room", "To provide staying at Non-AC room"),
            ("can_go_dehradoon", "Trip to Dehradoon"),
            ("can_go_mussoorie", "Trip to Mussoorie"),
            ("can_go_haridwaar", "Trip to Haridwaar"),
            ("can_go_rishikesh", "Trip to Rishikesh"))
