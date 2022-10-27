from django.contrib import admin

from .models import Benefactor, Charity, Task


@admin.register(Benefactor)
class BenefactorAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'experience', 'free_time_per_week',)
    list_filter = ('experience', 'user__gender',)


@admin.register(Charity)
class CharityAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'reg_number',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'state', 'assigned_benefactor',)
    list_display_links = ('title',)
    list_filter = ('state', 'gender_limit',)

    fieldsets = (
        ('Task', {
            'fields': (
                'title',
                'state',
                'description',
            )
        }),
        ('Members', {
            'fields': (
                'charity',
                'assigned_benefactor',
            )
        }),
        ('Task constraints', {
            'fields': (
                'date',
                'age_limit_from',
                'age_limit_to',
                'gender_limit',
            )
        }),
    )
