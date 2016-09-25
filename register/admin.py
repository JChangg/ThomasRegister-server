from django.contrib import admin
from models import Log


class LogAdmin(admin.ModelAdmin):
    model = Log
    list_display = ('time', 'get_person_name')
    readonly_fields = ('time',)
    fieldsets = (
        (None, {
            'fields':
                ('time', 'person', )
        }),
    )

    def get_person_name(self, obj):
        return "%s %s %s" % (
            obj.person.first_name,
            obj.person.middle_names,
            obj.person.last_name,
        )
    get_person_name.short_description = 'Person'

admin.site.register(Log, LogAdmin)
