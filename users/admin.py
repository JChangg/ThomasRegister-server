from django.contrib import admin
from models import Person, User, Card, ClassGroup
from register.models import Log
from django.contrib.auth.admin import UserAdmin as UserAdminBuiltIn

admin.site.site_title = 'TRegister'
admin.site.site_header = 'TRegister'


class LogInline(admin.StackedInline):
    model = Log
    extra = 0

class ClassGroupInline(admin.TabularInline):
    model = ClassGroup
    exclude = ('id', )


class CardInline(admin.TabularInline):
    model = Card
    extra = 1


class UserAdmin(UserAdminBuiltIn):
    readonly_fields = ('username',)
    fieldsets = (
        (None, {
            'fields':
                ('username', 'password', )
        }),
        ('Important dates', {
            'fields':
                ('last_login', 'date_joined')
        }),
        ('Advanced permissions', {
            'classes': ('collapse',),
            'fields': (
                'is_active',
                'is_superuser',
                'is_staff',
                'user_permissions',
            ),
        }),
    )


class UserInline(admin.StackedInline):
    model = User
    readonly_fields = ('username',)
    show_change_link = True
    fieldsets = (
        (None, {
            'fields':
                ('username', 'password', 'last_login', 'date_joined')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('is_superuser', 'is_staff', 'is_active'),
        }),
    )


class PersonAdmin(admin.ModelAdmin):

    inlines = [
        CardInline,
        UserInline,
        LogInline,
    ]

    list_display = ('username', 'first_name', 'last_name')

    exclude = ('username', )
    search_fields = ['first_name', 'middle_names', 'last_name']


admin.site.register(Person, PersonAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(ClassGroup)
