from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import Profile, CustomUser


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    """To allow users to access the django admin, set the role to is_staff.
    """
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
