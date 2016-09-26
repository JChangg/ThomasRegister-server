from django.contrib import admin
from models import Log


class LogAdmin(admin.ModelAdmin):
    model = Log
    list_display = (
        'time',
        'card',
        'get_person_name',
        'get_person_group',
    )

    list_filter = (
        'time',
        'card__person__group',
        'card__person__username',
    )
    search_fields = [
        'card__person__first_name',
        'card__person__middle_names',
        'card__person__last_name'
    ]
    readonly_fields = ('time',)
    fieldsets = (
        (None, {
            'fields':
                ('time', 'card', )
        }),
    )

    def get_person_name(self, obj):
        return "%s %s %s" % (
            obj.card.person.first_name,
            obj.card.person.middle_names,
            obj.card.person.last_name,
        )

    def get_person_group(self, obj):
        return obj.card.person.group.__str__() \
            if obj.card.person.group else 'N/A'

    get_person_name.short_description = 'Name'
    get_person_group.short_description = 'Year Group / Staff'

admin.site.register(Log, LogAdmin)
