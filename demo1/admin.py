from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.contrib import admin
from .models import *
from django.utils.translation import ugettext_lazy as _

def my_custom_action(modeladmin, request, queryset):

    for obj in queryset:
        subject = 'Thank you for registering for {}'.format(obj.eventname)
        body = 'Thank you for registering for {}.\nYour details are as follows:\nName: {}\nEmail: {}\nOrder ID: {}'.format(obj.eventname, obj.name, obj.email, obj.order_id)
        from_email = settings.EMAIL_HOST_USER
        to_email = obj.email
        msg = EmailMultiAlternatives(subject, body, from_email, [to_email])
        msg.attach_file(obj.file)
        msg.send()


my_custom_action.short_description = _("Send Email")



class Clientadmin(admin.ModelAdmin):
    list_display = ('client_name', 'contact_number')


class Participantadmin(admin.ModelAdmin):
    list_display = ('order_id', 'eventid', 'eventname', 'name', 'email', 'phonenumber')
    actions = [my_custom_action]



class Employeesadmin(admin.ModelAdmin):
    list_display = ('employee_id', 'first_name')


class Eventcat(admin.ModelAdmin):
    list_display = ('event_id', 'catgory_id')


admin.site.register(Employees, Employeesadmin)


class locationsinline(admin.StackedInline):
    model = Event_locations
    extra = 1

class SubLocationInline(admin.StackedInline):
    model = Sub_event
    extra = 0

class ticketinline(admin.StackedInline):
    model = tickettype
    extra = 1


class eventadmin(admin.ModelAdmin):
    inlines = [
        locationsinline, SubLocationInline, ticketinline
    ]

    add_form_template = 'admin/event_change_form.html'


    

admin.site.register(Categories)
admin.site.register(Event, eventadmin)
admin.site.register(Event_transaction)
admin.site.register(Event_locations)
admin.site.register(Event_category, Eventcat)
admin.site.register(Event_employees)
admin.site.register(Sub_event)
admin.site.register(Client, Clientadmin)
admin.site.register(Participant, Participantadmin)
admin.site.register(tickettype)





