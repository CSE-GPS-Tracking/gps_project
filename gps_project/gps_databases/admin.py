# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Role)
admin.site.register(Driver)

class BusAdmin(admin.ModelAdmin):
    list_display = ['bus_id','status','capacity']
admin.site.register(Bus,BusAdmin)

class RouteAdmin(admin.ModelAdmin):
    list_display = ['route_id','route_type','from_clg_estimated_start_time','from_clg_estimated_reach_time','to_clg_estimated_start_time','to_clg_estimated_reach_time']
admin.site.register(Route,RouteAdmin)

class AllocationAdmin(admin.ModelAdmin):
    list_display = ['bus_id','route_id','driver_id']
admin.site.register(Allocation)

class TrackingAdmin(admin.ModelAdmin):
    list_display = ['bus_id','route_id','driver_id','trip_direction','date','start_time','fuel_perc','refill','end_time','status','file_name']
admin.site.register(Tracking,TrackingAdmin)


admin.site.register(BusStop)
admin.site.register(BusTimes)
admin.site.register(Alert)
admin.site.register(AlertInfo)
admin.site.register(Ticket)
admin.site.register(TicketInfo)
admin.site.register(Sos)



