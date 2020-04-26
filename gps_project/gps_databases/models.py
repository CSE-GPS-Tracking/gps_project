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
	from_clg_estimated_reach_time = models.DateTimeField()
	from_clg_estimated_start_time = models.DateTimeField()
	to_clg_estimated_reach_time = models.DateTimeField()
	to_clg_estimated_start_time = models.DateTimeField()


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
    email_id = models.CharField(max_length=40)
    route_id = models.ForeignKey(Route)
    bus_stop_id = models.ForeignKey(BusStop)
    user_role_choices = [("Student","Student"),("Admin","Admin"),("Staff","Staff")]
    user_role = models.CharField(choices=user_role_choices,max_length=30)


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


class Tracking(models.Model):
	bus_id = models.ForeignKey(Bus)
	route_id = models.ForeignKey(Route)
	direction_choices = [("To College","To College"),("From College","From College")]
	trip_direction = models.CharField(max_length=20,choices=direction_choices)
	date = models.DateTimeField()
	start_time = models.DateTimeField()
	current_latitude = models.FloatField()
	current_longitude = models.FloatField()
	end_time = models.DateTimeField()
	status_choices = [("Ongoing","Ongoing"),("Terminated","Terminated"),("Completed","Completed")]
	status = models.CharField(choices=status_choices,max_length=30)
	driver_id = models.ForeignKey(Driver)


class AlertInfo(models.Model):
	alert_code = models.CharField(max_length=10,primary_key=True)
	alert_type = models.CharField(max_length=30)

class Alert(models.Model):
	alert_id = models.CharField(max_length=10,primary_key=True)
	alert_code = models.ForeignKey(AlertInfo)
	route_id = models.ForeignKey(Route)
	date = models.DateField()

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















