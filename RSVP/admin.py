from django.contrib import admin

from .models import Guest, GuestParty
# Register your models here.

class GuestPartyAdmin(admin.TabularInline):
    model = GuestParty

class GuestAdmin(admin.ModelAdmin):
    model = Guest
    inlines = [GuestPartyAdmin,]

admin.site.register(Guest, GuestAdmin)
