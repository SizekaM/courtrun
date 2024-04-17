from django.db import models
import uuid
from django.utils.timezone import now

# Create your models here.
class SummonOrder(models.Model):

    delivery_types = [
        ('Standard', 'Standard'),
        ('Priority', 'Priority'),     
    ]

    delivery_times = [
        ('08:00', '08:00'),
        ('08:30', '08:30'),
        ('09:00', '09:00'),
        ('09:30', '09:30'),
        ('10:00', '10:00'),
        ('10:30', '10:30'),
        ('11:00', '11:00'), 
        ('11:30', '11:30'),  
        ('12:00', '12:00'),
        ('12:30', '12:30'),
        ('13:00', '13:00'),
        ('13:30', '13:30'),
        ('14:00', '14:00'),
        ('14:30', '14:30'),
        ('15:00', '15:00'),  
        ('15:30', '15:30'),    
    ]

    payment_options = [
        ('Online payment', 'Online payment'),
        ('Cash on Delivery', 'Cash on Delivery'),
        #('Card on Delivery', 'Card on Delivery')
    ]

    order_id = models.CharField(verbose_name='Order ID', default=uuid.uuid4().hex[:12], max_length=12, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    pickup_address = models.CharField(verbose_name='Pickup Address', max_length=120)
    pickup_coordinates = models.CharField(verbose_name='Pickup Coordinates', max_length=50)
    pickup_spec = models.CharField(verbose_name='Pickup Address Specification', max_length=200)
    pickup_notes = models.TextField(verbose_name='Pickup Address Notes')
    sheriff_address = models.CharField(verbose_name='Sheriff Address', max_length=120)
    sheriff_coordinates = models.CharField(verbose_name='Sheriff Coordinates', max_length=50)
    sheriff_spec = models.CharField(verbose_name='Sheriff Address Specification', max_length=200)
    sheriff_notes = models.TextField(verbose_name='Sheriff Address Notes')
    casenumber_establishment_address = models.CharField(verbose_name='Case Number Establishment Address', max_length=120)
    casenumber_establishment_coordinates = models.CharField(verbose_name='Case Number Establishment Coordinates', max_length=50)
    casenumber_establishment_spec = models.CharField(verbose_name='Case Number Establishment Address Specification', max_length=200)
    casenumber_establishment_notes = models.TextField(verbose_name='Case Number Establishment Address Notes')
    sc_establishment_address = models.CharField(verbose_name='Stamped Copy Establishment Address', max_length=120)
    sc_establishment_coordinates = models.CharField(verbose_name='Stamped Copy Establishment Coordinates', max_length=50)
    sc_establishment_spec = models.CharField(verbose_name='Stamped Copy Establishment Address Specification', max_length=200)
    sc_establishment_notes = models.TextField(verbose_name='Stamped Copy Establishment Address Notes')
    ros_establishment_address = models.CharField(verbose_name='Return of Service Establishment Address', max_length=120)
    ros_establishment_coordinates = models.CharField(verbose_name='Return of Service Coordinates', max_length=50)
    ros_establishment_spec = models.CharField(verbose_name='Return of Service Establishment Address Specification', max_length=200)
    ros_establishment_notes = models.TextField(verbose_name='Return of Service Establishment Address Notes')
    name = models.CharField(verbose_name='Customer Name', max_length=100)
    email = models.EmailField(verbose_name='Customer Email')
    contact = models.CharField(verbose_name='Contact Number', max_length=10)
    delivery_date = models.DateField(verbose_name='Scheduled Date', default=now, blank=True)
    delivery_time = models.CharField(verbose_name='Scheduled Time', max_length=5, choices=delivery_times, blank=True)
    delivery_type = models.CharField(max_length=20, choices=delivery_types)
    standard_fee = models.CharField(max_length=10, verbose_name="Standard Fee", default="Physical Calculations required")
    priority_fee = models.CharField(max_length=10, verbose_name="Priority Fee", default="Physical Calculations required")
    #payment_options = models.CharField(verbose_name="Payment Options",choices=payment_options, default='Online payment', max_length=50)    
    flyer = models.IntegerField(verbose_name="Protective & confidential Flyer", choices=[(x, x) for x in range(0, 11)], default=0)

    def __str__(self):
        return str(self.order_id)



class ServeOrder(models.Model):
    delivery_types = [
        ('Standard', 'Standard'),
        ('Priority', 'Priority'),     
    ]

    delivery_times = [
        ('08:00', '08:00'),
        ('08:30', '08:30'),
        ('09:00', '09:00'),
        ('09:30', '09:30'),
        ('10:00', '10:00'),
        ('10:30', '10:30'),
        ('11:00', '11:00'), 
        ('11:30', '11:30'),  
        ('12:00', '12:00'),
        ('12:30', '12:30'),
        ('13:00', '13:00'),
        ('13:30', '13:30'),
        ('14:00', '14:00'),
        ('14:30', '14:30'),
        ('15:00', '15:00'),  
        ('15:30', '15:30'),    
    ]

    payment_options = [
        ('Online payment', 'Online payment'),
        ('Cash on Delivery', 'Cash on Delivery'),
        #('Card on Delivery', 'Card on Delivery')
    ]

    order_id = models.CharField(verbose_name='Order ID', default=uuid.uuid4().hex[:12], max_length=12, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    pickup_address = models.CharField(verbose_name='Pickup Address', max_length=120)
    pickup_coordinates = models.CharField(verbose_name='Pickup Coordinates', max_length=50)
    pickup_spec = models.CharField(verbose_name='Pickup Address Specification', max_length=200)
    pickup_notes = models.TextField(verbose_name='Pickup Address Notes')
    serve_establishment_address = models.CharField(verbose_name='Serve Establishment Address', max_length=120)
    serve_establishment_coordinates = models.CharField(verbose_name='Serve Establishment Coordinates', max_length=50)
    serve_establishment_spec = models.CharField(verbose_name='Serve Establishment Address Specification', max_length=200)
    serve_establishment_notes = models.TextField(verbose_name='Serve Establishment Address Notes')
    dropoff_address = models.CharField(verbose_name='DropOff Address', max_length=120)
    dropoff_coordinates = models.CharField(verbose_name='Dropoff Coordinates', max_length=50)
    dropoff_spec = models.CharField(verbose_name='DropOff Address Specification', max_length=200)
    dropoff_notes = models.TextField(verbose_name='DropOff Address Notes')
    name = models.CharField(verbose_name='Customer Name', max_length=100)
    email = models.EmailField(verbose_name='Customer Email')
    contact = models.CharField(verbose_name='Contact Number', max_length=10)
    delivery_date = models.DateField(verbose_name='Scheduled Date', default=now, blank=True)
    delivery_time = models.CharField(verbose_name='Scheduled Time', max_length=5, choices=delivery_times, blank=True)
    delivery_type = models.CharField(max_length=20, choices=delivery_types)
    standard_fee = models.CharField(max_length=10, verbose_name="Standard Fee", default="Physical Calculations required")
    priority_fee = models.CharField(max_length=10, verbose_name="Priority Fee", default="Physical Calculations required")
    #payment_options = models.CharField(verbose_name="Payment Options",choices=payment_options, default='Online payment', max_length=50)    
    flyer = models.IntegerField(verbose_name="Protective & confidential Flyer", choices=[(x, x) for x in range(0, 11)], default=0)

    def __str__(self):
        return str(self.order_id)



class NoticeOrder(models.Model):
    delivery_types = [
        ('Standard', 'Standard'),
        ('Priority', 'Priority'),     
    ]

    delivery_times = [
        ('08:00', '08:00'),
        ('08:30', '08:30'),
        ('09:00', '09:00'),
        ('09:30', '09:30'),
        ('10:00', '10:00'),
        ('10:30', '10:30'),
        ('11:00', '11:00'), 
        ('11:30', '11:30'),  
        ('12:00', '12:00'),
        ('12:30', '12:30'),
        ('13:00', '13:00'),
        ('13:30', '13:30'),
        ('14:00', '14:00'),
        ('14:30', '14:30'),
        ('15:00', '15:00'),  
        ('15:30', '15:30'),    
    ]

    payment_options = [
        ('Online payment', 'Online payment'),
        ('Cash on Delivery', 'Cash on Delivery'),
        #('Card on Delivery', 'Card on Delivery')
    ]

    order_id = models.CharField(verbose_name='Order ID', default=uuid.uuid4().hex[:12], max_length=12, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    pickup_address = models.CharField(verbose_name='Pickup Address', max_length=120)
    pickup_coordinates = models.CharField(verbose_name='Pickup Coordinates', max_length=50)
    pickup_spec = models.CharField(verbose_name='Pickup Address Specification', max_length=200)
    pickup_notes = models.TextField(verbose_name='Pickup Address Notes')
    stop1_address = models.CharField(verbose_name='Stop 1 Address', blank=True, max_length=120, default="N/A")
    stop1_coordinates = models.CharField(verbose_name='Stop1 Coordinates', max_length=50, blank=True)
    stop1_spec = models.CharField(verbose_name='Stop 1 Specification', max_length=200, default="N/A", blank=True)
    stop1_notes = models.TextField(verbose_name='Stop 1 Notes', default="N/A", blank=True)
    stop2_address = models.CharField(verbose_name='Stop 2 Address', max_length=120, default="N/A", blank=True)
    stop2_coordinates = models.CharField(verbose_name='Stop2 Coordinates', max_length=50, blank=True)
    stop2_spec = models.CharField(verbose_name='Stop 2 Specification', max_length=200, default="N/A", blank=True)
    stop2_notes = models.TextField(verbose_name='Stop 2 Notes', default="N/A", blank=True)
    stop3_address = models.CharField(verbose_name='Stop 3 Address', max_length=120, default="N/A", blank=True)
    stop3_coordinates = models.CharField(verbose_name='Stop3 Coordinates', max_length=50, blank=True)
    stop3_spec = models.CharField(verbose_name='Stop 3 Specification', max_length=200, default="N/A", blank=True)
    stop3_notes = models.TextField(verbose_name='Stop 3 Notes', default="N/A", blank=True)
    stop4_address = models.CharField(verbose_name='Stop 4 Address', max_length=120, default="N/A", blank=True)
    stop4_coordinates = models.CharField(verbose_name='Stop4 Coordinates', max_length=50, blank=True)
    stop4_spec = models.CharField(verbose_name='Stop 4 Specification', max_length=200, default="N/A", blank=True)
    stop4_notes = models.TextField(verbose_name='Stop 4 Notes', default="N/A", blank=True)
    stop5_address = models.CharField(verbose_name='Stop 5 Address', max_length=120, default="N/A", blank=True)
    stop5_coordinates = models.CharField(verbose_name='Stop5 Coordinates', max_length=50, blank=True)
    stop5_spec = models.CharField(verbose_name='Stop 5 Specification', max_length=200, default="N/A", blank=True)
    stop5_notes = models.TextField(verbose_name='Stop 5 Notes', default="N/A", blank=True)
    stop6_address = models.CharField(verbose_name='Stop 6 Address', max_length=120, default="N/A", blank=True)
    stop6_coordinates = models.CharField(verbose_name='Stop6 Coordinates', max_length=50, blank=True)
    stop6_spec = models.CharField(verbose_name='Stop 6 Specification', max_length=200, default="N/A", blank=True)
    stop6_notes = models.TextField(verbose_name='Stop 6 Notes', default="N/A", blank=True) 
    dropoff_address = models.CharField(verbose_name='DropOff Address', max_length=120)
    dropoff_coordinates = models.CharField(verbose_name='Dropoff Coordinates', max_length=50)
    dropoff_spec = models.CharField(verbose_name='DropOff Address Specification', max_length=200)
    dropoff_notes = models.TextField(verbose_name='DropOff Address Notes')
    name = models.CharField(verbose_name='Customer Name', max_length=100)
    email = models.EmailField(verbose_name='Customer Email')
    contact = models.CharField(verbose_name='Contact Number', max_length=10)
    delivery_date = models.DateField(verbose_name='Scheduled Date', default=now, blank=True)
    delivery_time = models.CharField(verbose_name='Scheduled Time', max_length=5, choices=delivery_times, blank=True)
    delivery_type = models.CharField(max_length=20, choices=delivery_types)
    standard_fee = models.CharField(max_length=30, verbose_name="Standard Fee", default="Physical Calculations required")
    priority_fee = models.CharField(max_length=30, verbose_name="Priority Fee", default="Physical Calculations required")
    #payment_options = models.CharField(verbose_name="Payment Options",choices=payment_options, default='Online payment', max_length=50)    
    flyer = models.IntegerField(verbose_name="Protective & confidential Flyer", choices=[(x, x) for x in range(0, 11)], default=0)

    def __str__(self):
        return str(self.order_id)



class FileOrder(models.Model):
    delivery_types = [
        ('Standard', 'Standard'),
        ('Priority', 'Priority'),     
    ]

    delivery_times = [
        ('08:00', '08:00'),
        ('08:30', '08:30'),
        ('09:00', '09:00'),
        ('09:30', '09:30'),
        ('10:00', '10:00'),
        ('10:30', '10:30'),
        ('11:00', '11:00'), 
        ('11:30', '11:30'),  
        ('12:00', '12:00'),
        ('12:30', '12:30'),
        ('13:00', '13:00'),
        ('13:30', '13:30'),
        ('14:00', '14:00'),
        ('14:30', '14:30'),
        ('15:00', '15:00'),  
        ('15:30', '15:30'),    
    ]

    payment_options = [
        ('Online payment', 'Online payment'),
        ('Cash on Delivery', 'Cash on Delivery'),
        #('Card on Delivery', 'Card on Delivery')
    ]

    order_id = models.CharField(verbose_name='Order ID', default=uuid.uuid4().hex[:12], max_length=12, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    pickup_address = models.CharField(verbose_name='Pickup Address', max_length=120)
    pickup_spec = models.CharField(verbose_name='Pickup Address Specification', max_length=200)
    pickup_notes = models.TextField(verbose_name='Pickup Address Notes')
    pickup_coordinates = models.CharField(verbose_name='Pickup Coordinates', max_length=50)
    file_establishment_address = models.CharField(verbose_name='File Establishment Address', max_length=120)
    file_establishment_spec = models.CharField(verbose_name='File Establishment Address Specification', max_length=200)
    file_establishment_coordinates = models.CharField(verbose_name='File Establishment Coordinates', max_length=50)
    file_establishment_notes = models.TextField(verbose_name='File Establishment Address Notes')
    filing_docs = models.IntegerField(choices=[(x, x) for x in range(1, 11)], default=0)
    dropoff_address = models.CharField(verbose_name='DropOff Address', max_length=120)
    dropoff_coordinates = models.CharField(verbose_name='Dropoff Coordinates', max_length=50)
    dropoff_spec = models.CharField(verbose_name='DropOff Address Specification', max_length=200)
    dropoff_notes = models.TextField(verbose_name='DropOff Address Notes')
    name = models.CharField(verbose_name='Customer Name', max_length=100)
    email = models.EmailField(verbose_name='Customer Email')
    contact = models.CharField(verbose_name='Contact Number', max_length=10)
    delivery_date = models.DateField(verbose_name='Scheduled Date', default=now, blank=True)
    delivery_time = models.CharField(verbose_name='Scheduled Time', max_length=5, choices=delivery_times, blank=True)
    delivery_type = models.CharField(max_length=20, choices=delivery_types)
    standard_fee = models.CharField(max_length=10, verbose_name="Standard Fee", default="Physical Calculations required")
    priority_fee = models.CharField(max_length=10, verbose_name="Priority Fee", default="Physical Calculations required")
    #payment_options = models.CharField(verbose_name="Payment Options",choices=payment_options, default='Online payment', max_length=50)    
    flyer = models.IntegerField(verbose_name="Protective & confidential Flyer", choices=[(x, x) for x in range(0, 11)], default=0)

    def __str__(self):
        return str(self.order_id)



class CorrespondenceOrder(models.Model):
    delivery_types = [
        ('Standard', 'Standard'),
        ('Priority', 'Priority'),     
    ]

    delivery_times = [
        ('08:00', '08:00'),
        ('08:30', '08:30'),
        ('09:00', '09:00'),
        ('09:30', '09:30'),
        ('10:00', '10:00'),
        ('10:30', '10:30'),
        ('11:00', '11:00'), 
        ('11:30', '11:30'),  
        ('12:00', '12:00'),
        ('12:30', '12:30'),
        ('13:00', '13:00'),
        ('13:30', '13:30'),
        ('14:00', '14:00'),
        ('14:30', '14:30'),
        ('15:00', '15:00'),  
        ('15:30', '15:30'),    
    ]

    payment_options = [
        ('Online payment', 'Online payment'),
        ('Cash on Delivery', 'Cash on Delivery'),
       # ('Card on Delivery', 'Card on Delivery')
    ]

    order_id = models.CharField(verbose_name='Order ID', default=uuid.uuid4().hex[:12], max_length=12, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    pickup_address = models.CharField(verbose_name='Pickup Address', max_length=120)
    pickup_coordinates = models.CharField(verbose_name='Pickup Coordinates', max_length=50)
    pickup_spec = models.CharField(verbose_name='Pickup Address Specification', max_length=200)
    pickup_notes = models.TextField(verbose_name='Pickup Address Notes')
    stop1_address = models.CharField(verbose_name='Stop 1 Address', blank=True, max_length=120, default="N/A")
    stop1_coordinates = models.CharField(verbose_name='Stop1 Coordinates', max_length=50, blank=True)
    stop1_spec = models.CharField(verbose_name='Stop 1 Specification', max_length=200, default="N/A", blank=True)
    stop1_notes = models.TextField(verbose_name='Stop 1 Notes', default="N/A", blank=True)
    stop2_address = models.CharField(verbose_name='Stop 2 Address', max_length=120, default="N/A", blank=True)
    stop2_coordinates = models.CharField(verbose_name='Stop2 Coordinates', max_length=50, blank=True)
    stop2_spec = models.CharField(verbose_name='Stop 2 Specification', max_length=200, default="N/A", blank=True)
    stop2_notes = models.TextField(verbose_name='Stop 2 Notes', default="N/A", blank=True)
    stop3_address = models.CharField(verbose_name='Stop 3 Address', max_length=120, default="N/A", blank=True)
    stop3_coordinates = models.CharField(verbose_name='Stop3 Coordinates', max_length=50, blank=True)
    stop3_spec = models.CharField(verbose_name='Stop 3 Specification', max_length=200, default="N/A", blank=True)
    stop3_notes = models.TextField(verbose_name='Stop 3 Notes', default="N/A", blank=True)
    stop4_address = models.CharField(verbose_name='Stop 4 Address', max_length=120, default="N/A", blank=True)
    stop4_coordinates = models.CharField(verbose_name='Stop4 Coordinates', max_length=50, blank=True)
    stop4_spec = models.CharField(verbose_name='Stop 4 Specification', max_length=200, default="N/A", blank=True)
    stop4_notes = models.TextField(verbose_name='Stop 4 Notes', default="N/A", blank=True)
    stop5_address = models.CharField(verbose_name='Stop 5 Address', max_length=120, default="N/A", blank=True)
    stop5_coordinates = models.CharField(verbose_name='Stop5 Coordinates', max_length=50, blank=True)
    stop5_spec = models.CharField(verbose_name='Stop 5 Specification', max_length=200, default="N/A", blank=True)
    stop5_notes = models.TextField(verbose_name='Stop 5 Notes', default="N/A", blank=True)
    stop6_address = models.CharField(verbose_name='Stop 6 Address', max_length=120, default="N/A", blank=True)
    stop6_coordinates = models.CharField(verbose_name='Stop6 Coordinates', max_length=50, blank=True)
    stop6_spec = models.CharField(verbose_name='Stop 6 Specification', max_length=200, default="N/A", blank=True)
    stop6_notes = models.TextField(verbose_name='Stop 6 Notes', default="N/A", blank=True) 
    dropoff_address = models.CharField(verbose_name='DropOff Address', max_length=120)
    dropoff_coordinates = models.CharField(verbose_name='Dropoff Coordinates', max_length=50)
    dropoff_spec = models.CharField(verbose_name='DropOff Address Specification', max_length=200)
    dropoff_notes = models.TextField(verbose_name='DropOff Address Notes')
    name = models.CharField(verbose_name='Customer Name', max_length=100)
    email = models.EmailField(verbose_name='Customer Email')
    contact = models.CharField(verbose_name='Contact Number', max_length=10)
    delivery_date = models.DateField(verbose_name='Scheduled Date', default=now, blank=True)
    delivery_time = models.CharField(verbose_name='Scheduled Time', max_length=5, choices=delivery_times, blank=True)
    delivery_type = models.CharField(max_length=20, choices=delivery_types)
    standard_fee = models.CharField(max_length=10, verbose_name="Standard Fee", default="Physical Calculations required")
    priority_fee = models.CharField(max_length=10, verbose_name="Priority Fee", default="Physical Calculations required")
    #payment_options = models.CharField(verbose_name="Payment Options",choices=payment_options, default='Online payment', max_length=50)    
    flyer = models.IntegerField(verbose_name="Protective & confidential Flyer", choices=[(x, x) for x in range(0, 11)], default=0)

    def __str__(self):
        return str(self.order_id)



class CollectionDropoffOrder(models.Model):
    
    delivery_types = [
        ('Standard', 'Standard'),
        ('Priority', 'Priority'),     
    ]

    delivery_times = [
        ('08:00', '08:00'),
        ('08:30', '08:30'),
        ('09:00', '09:00'),
        ('09:30', '09:30'),
        ('10:00', '10:00'),
        ('10:30', '10:30'),
        ('11:00', '11:00'), 
        ('11:30', '11:30'),  
        ('12:00', '12:00'),
        ('12:30', '12:30'),
        ('13:00', '13:00'),
        ('13:30', '13:30'),
        ('14:00', '14:00'),
        ('14:30', '14:30'),
        ('15:00', '15:00'),  
        ('15:30', '15:30'),    
    ]

    payment_options = [
        ('Online payment', 'Online payment'),
        ('Cash on Delivery', 'Cash on Delivery'),
       # ('Card on Delivery', 'Card on Delivery')
    ]
    
    order_id = models.CharField(verbose_name='Order ID', default=uuid.uuid4().hex[:12], max_length=12, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    pickup_address = models.CharField(verbose_name='Pickup Address', max_length=120)
    pickup_coordinates = models.CharField(verbose_name='Pickup Coordinates', max_length=50)
    pickup_spec = models.CharField(verbose_name='Pickup Address Specification', max_length=200)
    pickup_notes = models.TextField(verbose_name='Pickup Address Notes')
    stop1_address = models.CharField(verbose_name='Stop 1 Address', blank=True, max_length=120, default="N/A")
    stop1_coordinates = models.CharField(verbose_name='Stop1 Coordinates', max_length=50, blank=True)
    stop1_spec = models.CharField(verbose_name='Stop 1 Specification', max_length=200, default="N/A", blank=True)
    stop1_notes = models.TextField(verbose_name='Stop 1 Notes', default="N/A", blank=True)
    stop2_address = models.CharField(verbose_name='Stop 2 Address', max_length=120, default="N/A", blank=True)
    stop2_coordinates = models.CharField(verbose_name='Stop2 Coordinates', max_length=50, blank=True)
    stop2_spec = models.CharField(verbose_name='Stop 2 Specification', max_length=200, default="N/A", blank=True)
    stop2_notes = models.TextField(verbose_name='Stop 2 Notes', default="N/A", blank=True)
    stop3_address = models.CharField(verbose_name='Stop 3 Address', max_length=120, default="N/A", blank=True)
    stop3_coordinates = models.CharField(verbose_name='Stop3 Coordinates', max_length=50, blank=True)
    stop3_spec = models.CharField(verbose_name='Stop 3 Specification', max_length=200, default="N/A", blank=True)
    stop3_notes = models.TextField(verbose_name='Stop 3 Notes', default="N/A", blank=True)
    stop4_address = models.CharField(verbose_name='Stop 4 Address', max_length=120, default="N/A", blank=True)
    stop4_coordinates = models.CharField(verbose_name='Stop4 Coordinates', max_length=50, blank=True)
    stop4_spec = models.CharField(verbose_name='Stop 4 Specification', max_length=200, default="N/A", blank=True)
    stop4_notes = models.TextField(verbose_name='Stop 4 Notes', default="N/A", blank=True)
    stop5_address = models.CharField(verbose_name='Stop 5 Address', max_length=120, default="N/A", blank=True)
    stop5_coordinates = models.CharField(verbose_name='Stop5 Coordinates', max_length=50, blank=True)
    stop5_spec = models.CharField(verbose_name='Stop 5 Specification', max_length=200, default="N/A", blank=True)
    stop5_notes = models.TextField(verbose_name='Stop 5 Notes', default="N/A", blank=True)
    stop6_address = models.CharField(verbose_name='Stop 6 Address', max_length=120, default="N/A", blank=True)
    stop6_coordinates = models.CharField(verbose_name='Stop6 Coordinates', max_length=50, blank=True)
    stop6_spec = models.CharField(verbose_name='Stop 6 Specification', max_length=200, default="N/A", blank=True)
    stop6_notes = models.TextField(verbose_name='Stop 6 Notes', default="N/A", blank=True) 
    dropoff_address = models.CharField(verbose_name='DropOff Address', max_length=120)
    dropoff_coordinates = models.CharField(verbose_name='Dropoff Coordinates', max_length=50)
    dropoff_spec = models.CharField(verbose_name='DropOff Address Specification', max_length=200)
    dropoff_notes = models.TextField(verbose_name='DropOff Address Notes')
    name = models.CharField(verbose_name='Customer Name', max_length=100)
    email = models.EmailField(verbose_name='Customer Email')
    contact = models.CharField(verbose_name='Contact Number', max_length=10)
    delivery_date = models.DateField(verbose_name='Scheduled Date', default=now, blank=True)
    delivery_time = models.CharField(verbose_name='Scheduled Time', max_length=5, choices=delivery_times, blank=True)
    delivery_type = models.CharField(max_length=20, choices=delivery_types)
    standard_fee = models.CharField(max_length=10, verbose_name="Standard Fee", default="Physical Calculations required")
    priority_fee = models.CharField(max_length=10, verbose_name="Priority Fee", default="Physical Calculations required")
    #payment_options = models.CharField(verbose_name="Payment Options",choices=payment_options, default='Online payment', max_length=50)    
    flyer = models.IntegerField(verbose_name="Protective & confidential Flyer", choices=[(x, x) for x in range(0, 11)], default=0)

    def __str__(self):
        return str(self.order_id)



class Contact(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name='Name', max_length=100)
    email = models.EmailField(verbose_name='Email')
    number = models.CharField(verbose_name='Number', max_length=12)
    message = models.TextField(verbose_name='Message')

    def __str__(self):
        return str(self.name)