from django.contrib import admin
from .models import CustomUser, Profile


class ProfileModelAdmin(admin.ModelAdmin):
    """
    Show logged in super user their account only. Only super user can view all accounts
    """

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        if request.user.is_superuser:
            return qs.all()
        else:
            # FieldError then query for user to get profiles
            try:
                return qs.filter(profile__user=request.user)
            except:
                return qs.filter(user=request.user)


admin.site.register(Profile, ProfileModelAdmin)
admin.site.register(CustomUser, ProfileModelAdmin)
