from django.contrib import admin

from polls.models import Profile

class ProfileAdmin(admin.ModelAdmin):
    fields = ["user", "first_name", "last_name", "phone"]

admin.site.register(Profile, ProfileAdmin)
