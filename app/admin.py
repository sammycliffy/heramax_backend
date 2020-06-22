from django.contrib import admin
from .models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'account_number', 'bank', 'account_name']


class PlanAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount', 'interest', 'total',
                    'start_date', 'end_date', 'duration', 'is_approved', 'is_new', 'is_assigned']


class ReceiverAdmin(admin.ModelAdmin):
    list_display = ['person_to_pay', 'the_receiver', 'has_received', 'amount',
                    ]


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Plan, PlanAdmin)
admin.site.register(Receiver, ReceiverAdmin)
