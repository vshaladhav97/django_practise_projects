# from django.db import models

# # Create your models here.
# from django.contrib.auth.models import AbstractUser
# from django.utils import timezone
# from django.db import models
# from django.utils.translation import gettext as _



# class User(AbstractUser):
#     """Define the extra fields related to User here"""

#     first_name = models.CharField(
#         _('First Name of User'), blank=True, max_length=20)
#     last_name = models.CharField(
#         _('Last Name of User'), blank=True, max_length=20)
#     # - - - Some more User fields according to your need s

#     # This is the most important part to look upon to  define the custom permissions related to User.

#     class Meta:
#         permissions = (("can_go_in_non_ac_bus", "To provide non-AC Bus facility"),
#                         ("can_go_in_ac_bus", "To provide AC-Bus facility"),
#                         ("can_stay_ac-room", "To provide staying at AC room"),
#                         ("can_go_dehradoon", "Trip to Dehradoon"),
#                         ("can_go_mussoorie", "Trip to Mussoorie"),
#                         ("can_go_haridwaar", "Trip to Haridwaar"),
#                         ("can_go_rishikesh", "Trip to Rishikesh"))
