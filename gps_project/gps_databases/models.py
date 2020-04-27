# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models

class Bus(models.Model):
    """
    Each bus is treated as an entity with id being its Number-Plate and is assigned to a Route when working.
    This helps to track which bus is assigned to a specific route each day.

    --Attributes
    bus_id,status,capacity
    """
    bus_id= models.CharField(max_length=10,primary_key=True)
    status_choice = [("Working","Working"),("Damaged","Damaged"),("Dormant","Dormant")]
    status= models.CharField(choices=status_choice,max_length=30)
    capacity = models.IntegerField()


class Route(models.Model):
    """
    Routes indicate the bus numbers (46,64,12).

    --Attributes
    route_id,route_type
    """
    route_id = models.CharField(max_length=10,primary_key=True)
    type_choice = [("Staff","Staff"),("Student","Student"),("Other","Other")]
    route_type = models.CharField(choices=type_choice,max_length=30)
    from_clg_estimated_start_time = models.DateTimeField()
	from_clg_estimated_reach_time = models.DateTimeField()
	to_clg_estimated_start_time = models.DateTimeField()
	to_clg_estimated_reach_time = models.DateTimeField()
    #no_of_stops .. can be calculated ?
    #sample databases



class BusStop(models.Model):
	bus_stop_id = models.CharField(max_length=10,primary_key=True)
	bus_stop_name = models.CharField(max_length=30)
	latitude = models.FloatField()
	longitude = models.FloatField()


class BusTimes(models.Model):
	route_id = models.ForeignKey(Route)
	bus_stop_id = models.ForeignKey(BusStop)
    est_arr_time = models.TimeField() 
	


class User(models.Model):
    """
    This model facilitates creating a single login for three types of users.

    -- Roles : Student,Staff,Admin
    __ Attributes: user_id,password,firstName,lastName,phone,email_id,route_id,stop_id
    """
    user_id = models.CharField(max_length=20,primary_key=True)
    password= models.CharField(max_length=30)
    first_name= models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    email_id = models.CharField(max_length=40)
    route_id = models.ForeignKey(Route)
    bus_stop_id = models.ForeignKey(BusStop)
    created_date = models.DateField() #DateTimeField()?
    updated_date = models.DateField()
    role_id = models.ForeignKey(Role)
    sos_id = models.ForeignKey(Sos)


class Role(models.Model):
    role_id = models.CharField(max_length=10,primary_key=True)
    role_name = models.CharField(max_length=20)
    description = description = models.CharField(max_length=100)

class Driver(models.Model):
    """
    Drivers are separated from users since the attributes are different.
    Drivers are only registered/added and never deleted.

    --Attributes
    driver_id,first_name,last_name,joining_date,end_date (Last day of job)

    """
    driver_id = models.CharField(max_length=10,primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_no = models.CharField(max_length=10)
    joining_date = models.DateField()
    end_date= models.DateField()


class Allocation(models.Model):
    bus_id = models.ForeignKey(Bus)
    route_id = models.ForeignKey(Route)
    driver_id = models.ForeignKey(Driver)
    

class Tracking(models.Model):
	bus_id = models.ForeignKey(Bus)
	route_id = models.ForeignKey(Route)
	direction_choices = [("To College","To College"),("From College","From College"),("Other","Other")] #Other can be petrol,etc.
	trip_direction = models.CharField(max_length=20,choices=direction_choices)
	date = models.DateTimeField()
	start_time = models.DateTimeField()
    fuel_perc = models.FloatField()
    refill = models.BooleanField(default=False) 
    """If in a particular trip, the bus's fuel percentage increases from low to high, the
    refill attribute is set to be true as an indication of petrol being filled in that trip."""
	end_time = models.DateTimeField()
	status_choices = [("Ongoing","Ongoing"),("Terminated","Terminated"),("Completed","Completed")]
	status = models.CharField(choices=status_choices,max_length=30)
	file_name = FileField()
    """IN THIS FILE (EXCEL/CSV file), values such as time, lat, long, altitude, ignition, 
    battery are stored at regular and small intervals"""
    driver_id = models.ForeignKey(Driver)


class AlertInfo(models.Model):
	alert_code = models.CharField(max_length=10,primary_key=True)
	alert_type = models.CharField(max_length=30)
    #SMSalert_interval = models.IntegerField()
    #SMSalert_Max = models.IntegerField()


class Alert(models.Model):
	alert_id = models.CharField(max_length=10,primary_key=True)
	alert_code = models.ForeignKey(AlertInfo)
	route_id = models.ForeignKey(Route)
	date = models.DateField()
    time = models.TimeField()
    #status_choices = [("Resolved","Resolved"),("Pending","Pending")]
    #status = models.CharField(choices=status_choices,max_length=30)
    #reason = models.CharField(max_length=100)

class TicketInfo(models.Model):
	ticket_code = models.CharField(max_length=10,primary_key=True)
	ticket_type = models.CharField(max_length=30)

class Ticket(models.Model):
	ticket_id = models.CharField(max_length=10,primary_key=True)
	ticket_code = models.ForeignKey(TicketInfo)
	user_id = models.ForeignKey(User)
	description = models.CharField(max_length=100)
	route_id = models.ForeignKey(Route)
	date = models.DateField()
    time = models.TimeField()
    #status_choices = [("Resolved","Resolved"),("Pending","Pending")]
    #status = models.CharField(choices=status_choices,max_length=30)

class Sos(models.Model):
    sos_id = models.CharField(max_length=10,primary_key=True)
    sos_name1 = models.CharField(max_length=30)
    sos_phn_1 = models.CharField(max_length=10)
    sos_name2 = models.CharField(max_length=30)
    sos_phn_2 = models.CharField(max_length=10)










