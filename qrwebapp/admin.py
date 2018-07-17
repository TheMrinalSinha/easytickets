from django.contrib import admin
from .models        import Passenger, Ticket, Route, RazorpayPayment

# Register your models here.
class ReadOnlyMixin(object):
    allow_edits = ()
    calc_fields = ()

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_readonly_fields(self, request, obj=None):
        fields = [field.name for field in self.model._meta.fields
                  if field.name not in self.allow_edits]
        if self.calc_fields:
            fields.extend(self.calc_fields)
        return fields

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

@admin.register(RazorpayPayment)
class RazorpayAdmin(ReadOnlyMixin, admin.ModelAdmin):
    list_display = ('ticket', 'method', 'payment_status', 'captured', 'bank', 'wallet', 'vpa', 'created_at')
    list_filter  = ('payment_status', 'captured', 'method')

class TicketRazorPayment(ReadOnlyMixin, admin.TabularInline):
    model  = RazorpayPayment
    fields = ('method', 'payment_status', 'captured', 'bank', 'wallet', 'vpa', 'created_at')

@admin.register(Ticket)
class TicketAdmin(ReadOnlyMixin, admin.ModelAdmin):
    list_display = ('reference', 'passanger', 'source', 'destination', 'fare', 'created_on')
    inlines = [TicketRazorPayment]

admin.site.register(Passenger)
admin.site.register(Route)
