from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm,UserChangeForm
from .models import User
from django.contrib.auth.models import Group

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('email','full_name','is_admin','is_removed','is_active')
    list_filter = ('is_admin','is_removed')
    list_editable = ('is_removed','is_active')
    fieldsets = (
        ("Main",{'fields':('full_name','email','password')}),
        ("Activision Status",{'fields':('is_active','is_removed')}),
        ("Permissions",{'fields':('is_admin',)}),
    )
    add_fieldsets = (
        (None,{'fields':('full_name','email','password')}),
    )
    search_fields = ('email',)
    ordering = ('-email',)
    filter_horizontal = ()

admin.site.unregister(Group)