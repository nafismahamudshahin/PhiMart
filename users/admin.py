from django.contrib import admin
from users.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomAdminUser(UserAdmin):
    model = User
    list_display = ('email','first_name','last_name','is_active')
    list_filter = ('is_active','is_staff')
    ordering = ("email",)
    fieldsets = (
        (None,{'fields':('email','password')}),
        ("Personal Info",{'fields':('first_name','last_name','address','phone_number')}),
        ('Permissions',{'fields':('groups','user_permissions','is_staff','is_active','is_superuser')}),
        ('Importents Dates',{'fields':('last_login','date_joined')})
    )

    add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('email', 'first_name', 'last_name', 'phone_number', 'is_active', 'is_staff'),
    }),
)


admin.site.register(User,CustomAdminUser)