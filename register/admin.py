from django.contrib import admin
from models import Log


class LogAdmin(admin.ModelAdmin):
    model = Log
    list_display = (
        'time',
        'person',
        'get_person_name',
        'get_person_class_group',
    )

    list_filter = ('time', 'person__class_group', 'person__username', )
    search_fields = ['person__first_name', 'person__middle_names', 'person__last_name']
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

    def get_person_class_group(self, obj):
        return obj.person.class_group.__str__() \
            if obj.person.class_group else 'N/A'

    get_person_name.short_description = 'Name'
    get_person_class_group.short_description = 'Year Group / Staff'

admin.site.register(Log, LogAdmin)
