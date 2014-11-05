from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from accounts.models import Profile

# Define an inline admin descriptor for Profile model
# which acts a bit like a singleton
class UserProfileInline(admin.StackedInline):
    model = Profile
    can_delete = True
    max_num = 1

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

