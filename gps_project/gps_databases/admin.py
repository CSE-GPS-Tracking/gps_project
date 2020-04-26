# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Driver)

class BusAdmin(admin.ModelAdmin):
    list_display = ['bus_id','status','capacity']
admin.site.register(Bus,BusAdmin)

class RouteAdmin(admin.ModelAdmin):
    list_display = ['route_id','route_type']
admin.site.register(Route,RouteAdmin)

class TrackingAdmin(admin.ModelAdmin):
    list_display = ['bus_id','route_id','driver_id','trip_direction','date','start_time','end_time','current_latitude','current_longitude','status']
admin.site.register(Tracking,TrackingAdmin)

admin.site.register(BusStop)
admin.site.register(BusTimes)
admin.site.register(AlertInfo)
admin.site.register(Alert)
admin.site.register(TicketInfo)
admin.site.register(Ticket)



