from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect
from .forms import *
from .mixins import Directions
from django.core.mail import send_mail
from geopy.geocoders import GoogleV3
import uuid

geolocator = GoogleV3(api_key=settings.GOOGLE_API_KEY)


def home(request):
	return render(request, 'main/home.html')


def selection(request):
	return render(request, 'main/selection.html')


def route_serve(request):
	context = {"google_api_key": settings.GOOGLE_API_KEY}
	return render(request, 'main/route-serve.html', context)


def route_notice(request):
	context = {"google_api_key": settings.GOOGLE_API_KEY}
	return render(request, 'main/route-notice.html', context)


def route_correspondence(request):
	context = {"google_api_key": settings.GOOGLE_API_KEY}
	return render(request, 'main/route-correspondence.html', context)


def route_file(request):
	context = {"google_api_key": settings.GOOGLE_API_KEY}
	return render(request, 'main/route-file.html', context)


def route(request):
	context = {"google_api_key": settings.GOOGLE_API_KEY,}
	return render(request, 'main/route.html', context)


def route_summon(request):
	context = {"google_api_key": settings.GOOGLE_API_KEY,}
	return render(request, 'main/route-summon.html', context)


def map(request):

	lat_1 = request.GET.get("lat_1", None)
	long_1 = request.GET.get("long_1", None)
	lat_2 = request.GET.get("lat_2", None)
	long_2 = request.GET.get("long_2", None)
	lat_3 = request.GET.get("lat_3", None)
	long_3 = request.GET.get("long_3", None)
	lat_4 = request.GET.get("lat_4", None)
	long_4 = request.GET.get("long_4", None)
	lat_5 = request.GET.get("lat_5", None)
	long_5 = request.GET.get("long_5", None)
	lat_6 = request.GET.get("lat_6", None)
	long_6 = request.GET.get("long_6", None)
	lat_7 = request.GET.get("lat_7", None)
	long_7 = request.GET.get("long_7", None)
	lat_8 = request.GET.get("lat_8", None)
	long_8 = request.GET.get("long_8", None)


	lat_long_pairs = [
    (lat_1, long_1),
    (lat_2, long_2),
    (lat_3, long_3),
    (lat_4, long_4),
    (lat_5, long_5),
    (lat_6, long_6),
    (lat_7, long_7),
    (lat_8, long_8)
	]

	name_addresses = coordinate_converter(*lat_long_pairs)

	if lat_1 and lat_2:
		directions = Directions(
			lat_1= lat_1,
			long_1=long_1,
			lat_2 = lat_2,
			long_2=long_2,
			lat_3= lat_3,
			long_3=long_3,
			lat_4= lat_4,
			long_4=long_4,
			lat_5=lat_5,
			long_5=long_5,
			lat_6 = lat_6,
			long_6=long_6,
			lat_7= lat_7,
			long_7=long_7,
			long_8=long_8,
			lat_8=lat_8,
			)
		
	stops = directions["stops"]
	stop_number = []
	i = 0
	while i < stops:
		stop_number.append(i+1)
		i+=1

			
	stop_google_id = ["id-google-address-3", "id-google-address-4", "id-google-address-5", "id-google-address-6", "id-google-address-7", "id-google-address-8"]
	stop_name = ["stop1_address", "stop2_address", "stop3_address", "stop4_address", "stop5_address", "stop6_address"]
	stop_spec = ["stop1_spec", "stop2_spec", "stop3_spec", "stop4_spec", "stop5_spec", "stop6_spec"]
	stop_notes = ["stop1_notes", "stop2_notes", "stop3_notes", "stop4_notes", "stop5_notes", "stop6_notes"]
	stop_value = [name_addresses[2], name_addresses[3], name_addresses[4], name_addresses[5], name_addresses[6]]
	j = 0

	while j < stops:
		del stop_google_id[stops:]
		del stop_name[stops:]
		del stop_spec[stops:]
		del stop_value[stops:]
		del stop_notes[stops:]
		j+=1


	stop_info = zip(stop_number, stop_google_id, stop_name, stop_spec, stop_notes, stop_value)

	submitted = False
	if request.method == "POST":
		form = CollectionDropoffOrderForm(request.POST)

		if form.is_valid():
			form.save()
			orderId = form.cleaned_data.get('order_id')
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			pickup_address = form.cleaned_data['pickup_address']
			pickup_spec = form.cleaned_data['pickup_spec']
			pickup_notes = form.cleaned_data['pickup_notes']
			stop1_address = form.cleaned_data['stop1_address']
			stop1_spec = form.cleaned_data.get('stop1_spec')
			stop1_notes = form.cleaned_data.get('stop1_notes')
			stop2_address = form.cleaned_data.get('stop2_address')
			stop2_spec = form.cleaned_data.get('stop2_spec')
			stop2_notes = form.cleaned_data.get('stop2_notes')
			stop3_address = form.cleaned_data.get('stop3_address')
			stop3_spec = form.cleaned_data.get('stop3_spec')
			stop3_notes = form.cleaned_data.get('stop3_notes')
			stop4_address = form.cleaned_data.get('stop4_address')
			stop4_spec = form.cleaned_data.get('stop4_spec')
			stop4_notes = form.cleaned_data.get('stop4_notes')
			stop5_address = form.cleaned_data.get('stop5_address')
			stop5_spec = form.cleaned_data.get('stop5_spec')
			stop5_notes = form.cleaned_data.get('stop5_notes')
			stop6_address = form.cleaned_data.get('stop6_address')
			stop6_spec = form.cleaned_data.get('stop6_spec')
			stop6_notes = form.cleaned_data.get('stop6_notes')
			dropoff_address = form.cleaned_data['dropoff_address']
			dropoff_spec = form.cleaned_data['dropoff_spec']
			dropoff_notes = form.cleaned_data['dropoff_notes']
			contact_number = form.cleaned_data['contact']
			delivery_type  = form.cleaned_data['delivery_type']
			delivery_date = form.cleaned_data['delivery_date']
			delivery_time = form.cleaned_data['delivery_time']
			flyer = form.cleaned_data['flyer']
			standard_fee = form.cleaned_data['standard_fee']
			priority_fee = form.cleaned_data['priority_fee']
			

			stop_spec_list = []
			stop_notes_list = []
			if stop1_address:
				stop_spec_list.append(stop1_spec)
				stop_notes_list.append(stop1_notes)
				if stop2_address:
					stop_spec_list.append(stop2_spec)
					stop_notes_list.append(stop2_notes)
					if stop3_address:
						stop_spec_list.append(stop3_spec)
						stop_notes_list.append(stop3_notes)
						if stop4_address:
							stop_spec_list.append(stop4_spec)
							stop_notes_list.append(stop4_notes)
							if stop5_address:
								stop_spec_list.append(stop5_spec)
								stop_notes_list.append(stop5_notes)
								if stop6_address:
									stop_spec_list.append(stop6_spec)
									stop_notes_list.append(stop6_notes)
				


			message = f'Hi there {name}, \n\nThank you for choosing CourtRun Legal Couriers to deliver your documents.'
			message += f'\n\nPickup Address: {pickup_address} \n\nPickup Address Specifications: {pickup_spec} \n\nPickup Notes: {pickup_notes}' 

			for i in range(stops):
				message += f'\n\n\nStop{i+1} Address: {stop_value[i]} \n\nStop{i+1} Address Specifications: {stop_spec_list[i]} \n\nStop{i+1} Notes: {stop_notes_list[i]}'

			message += f'\n\n\nDrop-off Address: {dropoff_address} \n\nDrop Address Specifications: {dropoff_spec} \n\nDrop-off Notes: {dropoff_notes}' 
			message += f'\n\n\nContact Number: {contact_number} \n\nDelivery Type: {delivery_type}'
			message += f'\nScheduled Delivery Date: {delivery_date} \nScheduled Delivery Time: {delivery_time}'
			message += f'\n\nProtective & Confidential Sleeve: {flyer}'
			message += f'\n\n\nThe email containing the payment link will provide a detailed breakdown of the total price.'
			message += f'\n\nWarm Regards,\nCourtRun Sales Team.'

			send_mail(subject=f'CourtRun Collect & Dropff Order Confirmation #{orderId}',
					message=message,
					from_email=settings.EMAIL_HOST_USER,
					recipient_list=[email],
					fail_silently=True
					)



			messageAdmin = f'Hi there {name}, \n\nThank you for choosing CourtRun Legal Couriers to deliver your documents.'
			messageAdmin += f'\n\nPickup Address: {pickup_address} \n\nPickup Address Specifications: {pickup_spec} \n\nPickup Notes: {pickup_notes}' 
			
			for i in range(stops):
				message += f'\n\n\nStop{i+1} Address: {stop_value[i]} \n\nStop{i+1} Address Specifications: {stop_spec_list[i]} \n\nStop{i+1} Notes: {stop_notes_list[i]}'			
			
			messageAdmin += f'\n\n\nDrop-off Address: {dropoff_address} \n\nDrop Address Specifications: {dropoff_spec} \n\nDrop-off Notes: {dropoff_notes}' 
			messageAdmin += f'\n\n\nContact Number: {contact_number} \n\nDelivery Type: {delivery_type}'
			messageAdmin += f'\nScheduled Delivery Date: {delivery_date} \nScheduled Delivery Time: {delivery_time}'
			messageAdmin += f'\n\nProtective & Confidential Sleeve: {flyer}'
			messageAdmin += f'\n\n\n\n\n==FEES FROM ORDER =='
			messageAdmin += f'\n\nStandard fee: {standard_fee}'
			messageAdmin += f'\nPriority fee: {priority_fee}'

			send_mail(subject=f'CourtRun Collect & Dropff Order Confirmation #{orderId}',
					message=messageAdmin,
					from_email=settings.EMAIL_HOST_USER,
					recipient_list=['courtrun.orders@zektechnologies.co.za'],
					fail_silently=True
					)

			return HttpResponseRedirect('confirmation/')
		else:
			print(form.errors.as_data())
			form = CollectionDropoffOrderForm
			if 'submitted' in request.GET:
				submitted = True

	form = CollectionDropoffOrderForm


	context = {
		"google_api_key": settings.GOOGLE_API_KEY,
		"lat_1": lat_1,
		"long_1": long_1,
		"name_1": name_addresses[0],
		"lat_2": lat_2,
		"long_2": long_2,
		"name_2": name_addresses[1],
		"lat_3": lat_3,
		"long_3": long_3,
		"lat_4": lat_4,
		"long_4": long_4,
		"lat_5": lat_5,
		"long_5": long_5,
		"lat_6": lat_6,
		"long_6": long_6,
		"lat_7": lat_7,
		"long_7": long_7,
		"lat_8": lat_8,
		"long_8": long_8,
		"origin": f'{lat_1}, {long_1}',
		"destination": f'{lat_2}, {long_2}',
		"directions": directions,
		"form": form,
		"submitted": submitted,
		'stop_fields': range(0, stops), 
		"stop_info": stop_info,
		"order_id": uuid.uuid4().hex[:12],
		"Priority_Fee": float(directions["priority_fee"]) + (15 * stops), 
		"Standard_Fee": float(directions["standard_fee"]) + (15 * stops), 
		

		} 
	return render(request, 'main/map.html', context)


def map_summon(request):

	lat_1 = request.GET.get("lat_1", None)
	long_1 = request.GET.get("long_1", None)
	lat_2 = request.GET.get("lat_2", None)
	long_2 = request.GET.get("long_2", None)
	lat_3 = request.GET.get("lat_3", None)
	long_3 = request.GET.get("long_3", None)
	lat_4 = request.GET.get("lat_4", None)
	long_4 = request.GET.get("long_4", None)
	lat_5 = request.GET.get("lat_5", None)
	long_5 = request.GET.get("long_5", None)
	lat_6 = request.GET.get("lat_6", None)
	long_6 = request.GET.get("long_6", None)
	lat_7 = request.GET.get("lat_7", None)
	long_7 = request.GET.get("long_7", None)
	lat_8 = request.GET.get("lat_8", None)
	long_8 = request.GET.get("long_8", None)


	name_1 = geolocator.reverse(f'{lat_1}, {long_1}')
	name_2 = geolocator.reverse(f'{lat_2}, {long_2}')
	name_3 = geolocator.reverse(f'{lat_3}, {long_3}')
	name_4 = geolocator.reverse(f'{lat_4}, {long_4}')
	name_5 = geolocator.reverse(f'{lat_5}, {long_5}')

	if lat_1 and lat_2:
		directions = Directions(
			lat_1= lat_1,
			long_1=long_1,
			lat_2 = lat_2,
			long_2=long_2,
			lat_3= lat_3,
			long_3=long_3,
			lat_4= lat_4,
			long_4=long_4,
			lat_5=lat_5,
			long_5=long_5,
			lat_6 = lat_6,
			long_6=long_6,
			lat_7= lat_7,
			long_7=long_7,
			long_8=long_8,
			lat_8=lat_8,
			)
		
		submitted = False
		if request.method == "POST":
			form = SummonOrderForm(request.POST)

			if form.is_valid():
				form.save()
				orderId = form.cleaned_data['order_id']
				name = form.cleaned_data['name']
				email = form.cleaned_data['email']
				pickup_address = form.cleaned_data['pickup_address']
				pickup_spec = form.cleaned_data['pickup_spec']
				pickup_notes = form.cleaned_data['pickup_notes']
				casenumber_establishment_address = form.cleaned_data['casenumber_establishment_address']
				casenumber_establishment_spec = form.cleaned_data['casenumber_establishment_spec']
				casenumber_establishment_notes = form.cleaned_data['casenumber_establishment_notes']
				sheriff_address = form.cleaned_data['sheriff_address']
				sheriff_spec = form.cleaned_data['sheriff_spec']
				sheriff_notes = form.cleaned_data['sheriff_notes']
				sc_establishment_address = form.cleaned_data['sc_establishment_address']
				sc_establishment_spec = form.cleaned_data['sc_establishment_spec']
				sc_establishment_notes = form.cleaned_data['sc_establishment_notes']
				ros_establishment_address = form.cleaned_data['ros_establishment_address']
				ros_establishment_spec = form.cleaned_data['ros_establishment_spec']
				ros_establishment_notes = form.cleaned_data['ros_establishment_notes']
				contact_number = form.cleaned_data['contact']
				delivery_type  = form.cleaned_data['delivery_type']
				delivery_date = form.cleaned_data['delivery_date']
				delivery_time = form.cleaned_data['delivery_time']
				flyer = form.cleaned_data['flyer']
				standard_fee = form.cleaned_data['standard_fee']
				priority_fee = form.cleaned_data['priority_fee']


				send_mail(subject = f'CourtRun Summon Order Confirmation #{orderId}',
				message = f'Hi there {name}, \n\nThank you for choosing CourtRun Legal Couriers to deliver your documents.'
						f'\n\nPickup Address: {pickup_address} \n\nPickup Address Specifications: {pickup_spec} \n\nPickup Notes: {pickup_notes}' 
						f'\n\n\nCase Number Establishment Address: {casenumber_establishment_address} \n\nCase Number Establishment Address Specifications: {casenumber_establishment_spec} \n\nCase Number Establishment Notes: {casenumber_establishment_notes}'						
						f'\n\n\nSheriff Address: {sheriff_address} \n\nSheriff Address Specifications: {sheriff_spec} \n\nSheriff Notes: {sheriff_notes}' 						
						f'\n\n\nStamped Copy Establishment Address: {sc_establishment_address} \n\nStamped Copy Establishment Address Specifications: {sc_establishment_spec} \n\nStamped Copy Establishment Notes: {sc_establishment_notes}' 												
						f'\n\n\nReturn of Service Establishment Address: {ros_establishment_address} \n\nReturn of Service Establishment Address Specifications: {ros_establishment_spec} \n\nReturn of Service Establishment Notes: {ros_establishment_notes}' 																								
						f'\n\n\nContact Number: {contact_number} \n\nDelivery Type: {delivery_type}'
						f'\nScheduled Delivery Date: {delivery_date} \nScheduled Delivery Time: {delivery_time}'
						f'\n\nProtective & Confidential Sleeve: {flyer}'
						f'\n\n\nThe email containing the payment link will provide a detailed breakdown of the total price.'
						f'\n\nWarm Regards,\nCourtRun Sales Team.',
				from_email = settings.EMAIL_HOST_USER,
				recipient_list = [email],
				fail_silently=True
				)

				send_mail(subject = f'CourtRun Summon Order Confirmation #{orderId}',
				message = f'Hi there {name}, \n\nThank you for choosing CourtRun Legal Couriers to deliver your documents.'
						f'\n\nPickup Address: {pickup_address} \n\nPickup Address Specifications: {pickup_spec} \n\nPickup Notes: {pickup_notes}' 
						f'\n\n\nCase Number Establishment Address: {casenumber_establishment_address} \n\nCase Number Establishment Address Specifications: {casenumber_establishment_spec} \n\nCase Number Establishment Notes: {casenumber_establishment_notes}'						
						f'\n\n\nSheriff Address: {sheriff_address} \n\nSheriff Address Specifications: {sheriff_spec} \n\nSheriff Notes: {sheriff_notes}' 						
						f'\n\n\nStamped Copy Establishment Address: {sc_establishment_address} \n\nStamped Copy Establishment Address Specifications: {sc_establishment_spec} \n\nStamped Copy Establishment Notes: {sc_establishment_notes}' 												
						f'\n\n\nReturn of Service Establishment Address: {ros_establishment_address} \n\nReturn of Service Establishment Address Specifications: {ros_establishment_spec} \n\nReturn of Service Establishment Notes: {ros_establishment_notes}' 																		
						f'\n\n\nContact Number: {contact_number} \n\nDelivery Type: {delivery_type}'
						f'\nScheduled Delivery Date: {delivery_date} \nScheduled Delivery Time: {delivery_time}'						
						f'\n\nProtective & Confidential Sleeve: {flyer}'
						f'\n\n\n\n\n==FEES FROM ORDER =='
						f'\n\nStandard fee: {standard_fee}'
						f'\nPriority fee: {priority_fee}',
				from_email = settings.EMAIL_HOST_USER,
				recipient_list = ['courtrun.orders@zektechnologies.co.za'],
				fail_silently=True
				)

				return HttpResponseRedirect('confirmation/')
			else:
				form = SummonOrderForm
				if 'submitted' in request.GET:
					submitted = True

	form = SummonOrderForm


	context = {
	"google_api_key": settings.GOOGLE_API_KEY,
	"lat_1": lat_1,
	"long_1": long_1,
	'name_1': name_1.address,
	"lat_2": lat_2,
	"long_2": long_2,
	"name_2": name_2.address,
	"lat_3": lat_3,
	"long_3": long_3,
	'name_3': name_3.address,
	"lat_4": lat_4,
	"long_4": long_4,
	'name_4': name_4.address,
	"lat_5": lat_5,
	"long_5": long_5,
	'name_5': name_5.address,
	"origin": f'{lat_1}, {long_1}',
	"destination": f'{lat_2}, {long_2}',
	"directions": directions,
	"form": form,
	"submitted": submitted,
	"order_id": uuid.uuid4().hex[:12],
	"Priority_Fee": float(directions["priority_fee"]) + 50, 
	"Standard_Fee": float(directions["standard_fee"]) + 50, 

	}
	return render(request, 'main/map-summon.html', context)


def map_serve(request):

	lat_1 = request.GET.get("lat_1", None)
	long_1 = request.GET.get("long_1", None)
	lat_2 = request.GET.get("lat_2", None)
	long_2 = request.GET.get("long_2", None)
	lat_3 = request.GET.get("lat_3", None)
	long_3 = request.GET.get("long_3", None)
	lat_4 = request.GET.get("lat_4", None)
	long_4 = request.GET.get("long_4", None)
	lat_5 = request.GET.get("lat_5", None)
	long_5 = request.GET.get("long_5", None)
	lat_6 = request.GET.get("lat_6", None)
	long_6 = request.GET.get("long_6", None)
	lat_7 = request.GET.get("lat_7", None)
	long_7 = request.GET.get("long_7", None)
	lat_8 = request.GET.get("lat_8", None)
	long_8 = request.GET.get("long_8", None)

	name_1 = geolocator.reverse(f'{lat_1}, {long_1}')
	name_2 = geolocator.reverse(f'{lat_2}, {long_2}')
	name_3 = geolocator.reverse(f'{lat_3}, {long_3}')


	if lat_1 and lat_2:
		directions = Directions(
			lat_1= lat_1,
			long_1=long_1,
			lat_2 = lat_2,
			long_2=long_2,
			lat_3= lat_3,
			long_3=long_3,
			lat_4= lat_4,
			long_4=long_4,
			lat_5=lat_5,
			long_5=long_5,
			lat_6 = lat_6,
			long_6=long_6,
			lat_7= lat_7,
			long_7=long_7,
			long_8=long_8,
			lat_8=lat_8,
			)
		
		submitted = False
		if request.method == "POST":
			form = ServeOrderForm(request.POST)

			if form.is_valid():
				form.save()
				orderId = form.cleaned_data['order_id']
				name = form.cleaned_data['name']
				email = form.cleaned_data['email']
				pickup_address = form.cleaned_data['pickup_address']
				pickup_spec = form.cleaned_data['pickup_spec']
				pickup_notes = form.cleaned_data['pickup_notes']
				serve_establishment_address = form.cleaned_data.get('serve_establishment_address')
				serve_establishment_spec = form.cleaned_data.get('serve_establishment_spec')
				serve_establishment_notes = form.cleaned_data.get('serve_establishment_notes')
				dropoff_address = form.cleaned_data['dropoff_address']
				dropoff_spec = form.cleaned_data['dropoff_spec']
				dropoff_notes = form.cleaned_data['dropoff_notes']
				contact_number = form.cleaned_data['contact']
				delivery_type  = form.cleaned_data['delivery_type']
				delivery_date = form.cleaned_data['delivery_date']
				delivery_time = form.cleaned_data['delivery_time']
				flyer = form.cleaned_data['flyer']
				standard_fee = form.cleaned_data['standard_fee']
				priority_fee = form.cleaned_data['priority_fee']


				send_mail(subject = f'CourtRun Serve Order Confirmation #{orderId}',
				message = f'Hi there {name}, \n\nThank you for choosing CourtRun Legal Couriers to deliver your documents.'
						f'\n\nPickup Address: {pickup_address} \n\nPickup Address Specifications: {pickup_spec} \n\nPickup Notes: {pickup_notes}' 
						f'\n\n\nAddress/Name of Establishment To Serve Documents: {serve_establishment_address} \n\Serve Address Specifications: {serve_establishment_spec} \n\nServe Notes: {serve_establishment_notes}' 
						f'\n\n\nDrop-off Address: {dropoff_address} \n\nDrop Address Specifications: {dropoff_spec} \n\nDrop-off Notes: {dropoff_notes}' 
						f'\n\n\nContact Number: {contact_number} \n\nDelivery Type: {delivery_type}'
						f'\nScheduled Delivery Date: {delivery_date} \nScheduled Delivery Time: {delivery_time}'
						f'\n\nProtective & Confidential Sleeve: {flyer}'
						f'\n\n\nThe email containing the payment link will provide a detailed breakdown of the total price.'
						f'\n\nWarm Regards,\nCourtRun Sales Team.',
				from_email = settings.EMAIL_HOST_USER,
				recipient_list = [email],
				fail_silently=True
				)

				send_mail(subject = f'CourtRun Serve Order Confirmation #{orderId}',
				message = f'Hi there {name}, \n\nThank you for choosing CourtRun Legal Couriers to deliver your documents.'
						f'\n\nPickup Address/Name For Collection Of Documents To Be Served: {pickup_address} \n\nPickup Address Specifications: {pickup_spec} \n\nPickup Notes: {pickup_notes}' 
						f'\n\n\nAddress/Name of Establishment To Serve Documents: {serve_establishment_address} \n\Serve Address Specifications: {serve_establishment_spec} \n\nServe Notes: {serve_establishment_notes}' 
						f'\n\n\nDrop-off Address: {dropoff_address} \n\nDrop Address Specifications: {dropoff_spec} \n\nDrop-off Notes: {dropoff_notes}' 
						f'\n\n\nContact Number: {contact_number} \n\nDelivery Type: {delivery_type}'
						f'\nScheduled Delivery Date: {delivery_date} \nScheduled Delivery Time: {delivery_time}'
						f'\n\nProtective & Confidential Sleeve: {flyer}'
						f'\n\n\n\n\n==FEES FROM ORDER =='
						f'\n\nStandard fee: {standard_fee}'
						f'\nPriority fee: {priority_fee}',
				from_email = settings.EMAIL_HOST_USER,
				recipient_list = ['courtrun.orders@zektechnologies.co.za'],
				fail_silently=True
				)

				return HttpResponseRedirect('confirmation/')
			else:
				form = ServeOrderForm
				if 'submitted' in request.GET:
					submitted = True

	form = ServeOrderForm


	context = {
	"google_api_key": settings.GOOGLE_API_KEY,
	"lat_1": lat_1,
	"long_1": long_1,
	'name_1': name_1.address,
	"lat_2": lat_2,
	"long_2": long_2,
	"name_2": name_2.address,
	"lat_3": lat_3,
	"long_3": long_3,
	'name_3': name_3.address,
	"origin": f'{lat_1}, {long_1}',
	"destination": f'{lat_2}, {long_2}',
	"directions": directions,
	"form": form,
	"submitted": submitted,
	"order_id": uuid.uuid4().hex[:12],
	"Priority_Fee": float(directions["priority_fee"]) + 20, 
	"Standard_Fee": float(directions["standard_fee"])  + 20, 

	}
	return render(request, 'main/map-serve.html', context)


def map_correspondence(request):

	lat_1 = request.GET.get("lat_1", None)
	long_1 = request.GET.get("long_1", None)
	lat_2 = request.GET.get("lat_2", None)
	long_2 = request.GET.get("long_2", None)
	lat_3 = request.GET.get("lat_3", None)
	long_3 = request.GET.get("long_3", None)
	lat_4 = request.GET.get("lat_4", None)
	long_4 = request.GET.get("long_4", None)
	lat_5 = request.GET.get("lat_5", None)
	long_5 = request.GET.get("long_5", None)
	lat_6 = request.GET.get("lat_6", None)
	long_6 = request.GET.get("long_6", None)
	lat_7 = request.GET.get("lat_7", None)
	long_7 = request.GET.get("long_7", None)
	lat_8 = request.GET.get("lat_8", None)
	long_8 = request.GET.get("long_8", None)

	lat_long_pairs = [
    (lat_1, long_1),
    (lat_2, long_2),
    (lat_3, long_3),
    (lat_4, long_4),
    (lat_5, long_5),
    (lat_6, long_6),
    (lat_7, long_7),
    (lat_8, long_8)
	]

	name_addresses = coordinate_converter(*lat_long_pairs)


	if lat_1 and lat_2:
		directions = Directions(
			lat_1= lat_1,
			long_1=long_1,
			lat_2 = lat_2,
			long_2=long_2,
			lat_3= lat_3,
			long_3=long_3,
			lat_4= lat_4,
			long_4=long_4,
			lat_5=lat_5,
			long_5=long_5,
			lat_6 = lat_6,
			long_6=long_6,
			lat_7= lat_7,
			long_7=long_7,
			long_8=long_8,
			lat_8=lat_8,
			)

	stops = directions["stops"]
	stop_number = []
	i = 0
	while i < stops:
		stop_number.append(i+1)
		i+=1

			
	stop_google_id = ["id-google-address-3", "id-google-address-4", "id-google-address-5", "id-google-address-6", "id-google-address-7", "id-google-address-8"]
	stop_name = ["stop1_address", "stop2_address", "stop3_address", "stop4_address", "stop5_address", "stop6_address"]
	stop_spec = ["stop1_spec", "stop2_spec", "stop3_spec", "stop4_spec", "stop5_spec", "stop6_spec"]
	stop_notes = ["stop1_notes", "stop2_notes", "stop3_notes", "stop4_notes", "stop5_notes", "stop6_notes"]
	stop_value = [name_addresses[2], name_addresses[3], name_addresses[4], name_addresses[5], name_addresses[6]]
	j = 0

	while j < stops:
		del stop_google_id[stops:]
		del stop_name[stops:]
		del stop_spec[stops:]
		del stop_value[stops:]
		del stop_notes[stops:]
		j+=1


	stop_info = zip(stop_number, stop_google_id, stop_name, stop_spec, stop_notes, stop_value)
		
	submitted = False
	if request.method == "POST":
		form = CorrespondenceOrderForm(request.POST)

		if form.is_valid():
			form.save()
			orderId = form.cleaned_data['order_id']
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			pickup_address = form.cleaned_data['pickup_address']
			pickup_spec = form.cleaned_data['pickup_spec']
			pickup_notes = form.cleaned_data['pickup_notes']
			stop1_address = form.cleaned_data.get('stop1_address')
			stop1_spec = form.cleaned_data.get('stop1_spec')
			stop1_notes = form.cleaned_data.get('stop1_notes')
			stop2_address = form.cleaned_data.get('stop2_address')
			stop2_spec = form.cleaned_data.get('stop2_spec')
			stop2_notes = form.cleaned_data.get('stop2_notes')
			stop3_address = form.cleaned_data.get('stop3_address')
			stop3_spec = form.cleaned_data.get('stop3_spec')
			stop3_notes = form.cleaned_data.get('stop3_notes')
			stop4_address = form.cleaned_data.get('stop4_address')
			stop4_spec = form.cleaned_data.get('stop4_spec')
			stop4_notes = form.cleaned_data.get('stop4_notes')
			stop5_address = form.cleaned_data.get('stop5_address')
			stop5_spec = form.cleaned_data.get('stop5_spec')
			stop5_notes = form.cleaned_data.get('stop5_notes')
			stop6_address = form.cleaned_data.get('stop6_address')
			stop6_spec = form.cleaned_data.get('stop6_spec')
			stop6_notes = form.cleaned_data.get('stop6_notes')
			dropoff_address = form.cleaned_data['dropoff_address']
			dropoff_spec = form.cleaned_data['dropoff_spec']
			dropoff_notes = form.cleaned_data['dropoff_notes']
			contact_number = form.cleaned_data['contact']
			delivery_type  = form.cleaned_data['delivery_type']
			delivery_date = form.cleaned_data['delivery_date']
			delivery_time = form.cleaned_data['delivery_time']
			flyer = form.cleaned_data['flyer']
			standard_fee = form.cleaned_data['standard_fee']
			priority_fee = form.cleaned_data['priority_fee']
			

			stop_spec_list = []
			stop_notes_list = []
			if stop1_address:
				stop_spec_list.append(stop1_spec)
				stop_notes_list.append(stop1_notes)
				if stop2_address:
					stop_spec_list.append(stop2_spec)
					stop_notes_list.append(stop2_notes)
					if stop3_address:
						stop_spec_list.append(stop3_spec)
						stop_notes_list.append(stop3_notes)
						if stop4_address:
							stop_spec_list.append(stop4_spec)
							stop_notes_list.append(stop4_notes)
							if stop5_address:
								stop_spec_list.append(stop5_spec)
								stop_notes_list.append(stop5_notes)
								if stop6_address:
									stop_spec_list.append(stop6_spec)
									stop_notes_list.append(stop6_notes)
				


			message = f'Hi there {name}, \n\nThank you for choosing CourtRun Legal Couriers to deliver your documents.'
			message += f'\n\nPickup Address: {pickup_address} \n\nPickup Address Specifications: {pickup_spec} \n\nPickup Notes: {pickup_notes}' 

			for i in range(stops):
				message += f'\n\n\nStop{i+1} Address: {stop_value[i]} \n\nStop{i+1} Address Specifications: {stop_spec_list[i]} \n\nStop{i+1} Notes: {stop_notes_list[i]}'

			message += f'\n\n\nDrop-off Address: {dropoff_address} \n\nDrop Address Specifications: {dropoff_spec} \n\nDrop-off Notes: {dropoff_notes}' 
			message += f'\n\n\nContact Number: {contact_number} \n\nDelivery Type: {delivery_type}'
			message += f'\nScheduled Delivery Date: {delivery_date} \nScheduled Delivery Time: {delivery_time}'
			message += f'\n\nProtective & Confidential Sleeve: {flyer}'
			message += f'\n\n\nThe email containing the payment link will provide a detailed breakdown of the total price.'
			message += f'\n\nWarm Regards,\nCourtRun Sales Team.'

			send_mail(subject=f'CourtRun Correspondence Order Confirmation #{orderId}',
					message=message,
					from_email=settings.EMAIL_HOST_USER,
					recipient_list=[email],
					fail_silently=True
					)



			messageAdmin = f'Hi there {name}, \n\nThank you for choosing CourtRun Legal Couriers to deliver your documents.'
			messageAdmin += f'\n\nPickup Address: {pickup_address} \n\nPickup Address Specifications: {pickup_spec} \n\nPickup Notes: {pickup_notes}' 
			
			for i in range(stops):
				message += f'\n\n\nStop{i+1} Address: {stop_value[i]} \n\nStop{i+1} Address Specifications: {stop_spec_list[i]} \n\nStop{i+1} Notes: {stop_notes_list[i]}'			
			
			messageAdmin += f'\n\n\nDrop-off Address: {dropoff_address} \n\nDrop Address Specifications: {dropoff_spec} \n\nDrop-off Notes: {dropoff_notes}' 
			messageAdmin += f'\n\n\nContact Number: {contact_number} \n\nDelivery Type: {delivery_type}'
			messageAdmin += f'\nScheduled Delivery Date: {delivery_date} \nScheduled Delivery Time: {delivery_time}'
			messageAdmin += f'\n\nProtective & Confidential Sleeve: {flyer}'
			messageAdmin += f'\n\n\n\n\n==FEES FROM ORDER =='
			messageAdmin += f'\n\nStandard fee: {standard_fee}'
			messageAdmin += f'\nPriority fee: {priority_fee}'

			send_mail(subject=f'CourtRun Correspondence Order Confirmation #{orderId}',
					message=messageAdmin,
					from_email=settings.EMAIL_HOST_USER,
					recipient_list=['courtrun.orders@zektechnologies.co.za'],
					fail_silently=True
					)


			return HttpResponseRedirect('confirmation/')
		else:
			form = CorrespondenceOrderForm
			if 'submitted' in request.GET:
				submitted = True

	form = CorrespondenceOrderForm


	context = {
	"google_api_key": settings.GOOGLE_API_KEY,
	"lat_1": lat_1,
	"long_1": long_1,
	'name_1': name_addresses[0],
	"lat_2": lat_2,
	"long_2": long_2,
	"name_2": name_addresses[1],
	"lat_3": lat_3,
	"long_3": long_3,
	"lat_4": lat_4,
	"long_4": long_4,
	"lat_5": lat_5,
	"long_5": long_5,
	"lat_6": lat_6,
	"long_6": long_6,
	"lat_7": lat_7,
	"long_7": long_7,
	"lat_8": lat_8,
	"long_8": long_8,
	"stop_info": stop_info,
	"origin": f'{lat_1}, {long_1}',
	"destination": f'{lat_2}, {long_2}',
	"directions": directions,
	"form": form,
	"submitted": submitted,
	"order_id": uuid.uuid4().hex[:12],
	"Priority_Fee": float(directions["priority_fee"]) + (15 * stops), 
	"Standard_Fee": float(directions["standard_fee"]) + (15 * stops), 

	}
	return render(request, 'main/map-correspondence.html', context)


def map_file(request):

	lat_1 = request.GET.get("lat_1", None)
	long_1 = request.GET.get("long_1", None)
	lat_2 = request.GET.get("lat_2", None)
	long_2 = request.GET.get("long_2", None)
	lat_3 = request.GET.get("lat_3", None)
	long_3 = request.GET.get("long_3", None)
	lat_4 = request.GET.get("lat_4", None)
	long_4 = request.GET.get("long_4", None)
	lat_5 = request.GET.get("lat_5", None)
	long_5 = request.GET.get("long_5", None)
	lat_6 = request.GET.get("lat_6", None)
	long_6 = request.GET.get("long_6", None)
	lat_7 = request.GET.get("lat_7", None)
	long_7 = request.GET.get("long_7", None)
	lat_8 = request.GET.get("lat_8", None)
	long_8 = request.GET.get("long_8", None)


	name_1 = geolocator.reverse(f'{lat_1}, {long_1}')
	name_2 = geolocator.reverse(f'{lat_2}, {long_2}')
	name_3 = geolocator.reverse(f'{lat_3}, {long_3}')
	

	if lat_1 and lat_2:
		directions = Directions(
			lat_1= lat_1,
			long_1=long_1,
			lat_2 = lat_2,
			long_2=long_2,
			lat_3= lat_3,
			long_3=long_3,
			lat_4= lat_4,
			long_4=long_4,
			lat_5=lat_5,
			long_5=long_5,
			lat_6 = lat_6,
			long_6=long_6,
			lat_7= lat_7,
			long_7=long_7,
			long_8=long_8,
			lat_8=lat_8,
			)
		
		submitted = False
		if request.method == "POST":
			form = FileOrderForm(request.POST)

			if form.is_valid():
				form.save()
				orderId = form.cleaned_data.get('order_id')
				name = form.cleaned_data['name']
				email = form.cleaned_data['email']
				pickup_address = form.cleaned_data['pickup_address']
				pickup_spec = form.cleaned_data['pickup_spec']
				pickup_notes = form.cleaned_data['pickup_notes']
				file_establishment_address = form.cleaned_data.get('file_establishment_address')
				file_establishment_spec = form.cleaned_data.get('file_establishment_spec')
				file_establishment_notes = form.cleaned_data.get('file_establishment_notes')
				dropoff_address = form.cleaned_data['dropoff_address']
				dropoff_spec = form.cleaned_data['dropoff_spec']
				dropoff_notes = form.cleaned_data['dropoff_notes']
				contact_number = form.cleaned_data['contact']
				delivery_type  = form.cleaned_data['delivery_type']
				delivery_date = form.cleaned_data['delivery_date']
				delivery_time = form.cleaned_data['delivery_time']
				flyer = form.cleaned_data['flyer']
				standard_fee = form.cleaned_data['standard_fee']
				priority_fee = form.cleaned_data['priority_fee']


				send_mail(subject = f'CourtRun File Order Confirmation #{orderId}',
				message = f'Hi there {name}, \n\nThank you for choosing CourtRun Legal Couriers to deliver your documents.'
						f'\n\nPickup Address: {pickup_address} \n\nPickup Address Specifications: {pickup_spec} \n\nPickup Notes: {pickup_notes}' 
						f'\n\n\nAddress/Name of Establishment To File Documents: {file_establishment_address} \n\nFile Address Specifications: {file_establishment_spec} \n\nFile Notes: {file_establishment_notes}' 
						f'\n\n\nDrop-off Address: {dropoff_address} \n\nDrop Address Specifications: {dropoff_spec} \n\nDrop-off Notes: {dropoff_notes}' 
						f'\n\n\nContact Number: {contact_number} \n\nDelivery Type: {delivery_type}'
						f'\nScheduled Delivery Date: {delivery_date} \nScheduled Delivery Time: {delivery_time}'
						f'\n\nProtective & Confidential Sleeve: {flyer}'
						f'\n\n\nThe email containing the payment link will provide a detailed breakdown of the total price.'
						f'\n\nWarm Regards,\nCourtRun Sales Team.',
				from_email = settings.EMAIL_HOST_USER,
				recipient_list = [email],
				fail_silently=True
				)

				send_mail(subject = f'CourtRun File Order Confirmation #{orderId}',
				message = f'Hi there {name}, \n\nThank you for choosing CourtRun Legal Couriers to deliver your documents.'
						f'\n\nPickup Address/Name For Collection Of Documents To Be Served: {pickup_address} \n\nPickup Address Specifications: {pickup_spec} \n\nPickup Notes: {pickup_notes}' 
						f'\n\n\nAddress/Name of Establishment To File Documents: {file_establishment_address} \n\nFile Address Specifications: {file_establishment_spec} \n\nFile Notes: {file_establishment_notes}' 
						f'\n\n\nDrop-off Address: {dropoff_address} \n\nDrop Address Specifications: {dropoff_spec} \n\nDrop-off Notes: {dropoff_notes}' 
						f'\n\n\nContact Number: {contact_number} \n\nDelivery Type: {delivery_type}'
						f'\nScheduled Delivery Date: {delivery_date} \nScheduled Delivery Time: {delivery_time}'
						f'\n\nProtective & Confidential Sleeve: {flyer}'
						f'\n\n\n\n\n==FEES FROM ORDER =='
						f'\n\nStandard fee: {standard_fee}'
						f'\nPriority fee: {priority_fee}',
				from_email = settings.EMAIL_HOST_USER,
				recipient_list = ['courtrun.orders@zektechnologies.co.za'],
				fail_silently=True
				)

				return HttpResponseRedirect('confirmation/')
			
			else:
				form = FileOrderForm
				if 'submitted' in request.GET:
					submitted = True

	form = FileOrderForm


	context = {
	"google_api_key": settings.GOOGLE_API_KEY,
	"lat_1": lat_1,
	"long_1": long_1,
	'name_1': name_1.address,
	"lat_2": lat_2,
	"long_2": long_2,
	"name_2": name_2.address,
	"lat_3": lat_3,
	"long_3": long_3,
	'name_3': name_3.address,
	"origin": f'{lat_1}, {long_1}',
	"destination": f'{lat_2}, {long_2}',
	"directions": directions,
	"form": form,
	"submitted": submitted,
	"order_id": uuid.uuid4().hex[:12],
	"Priority_Fee": float(directions["priority_fee"]) + 25, 
	"Standard_Fee": float(directions["standard_fee"]) +25, 

	}
	return render(request, 'main/map-file.html', context)


def map_notice(request):

	lat_1 = request.GET.get("lat_1", None)
	long_1 = request.GET.get("long_1", None)
	lat_2 = request.GET.get("lat_2", None)
	long_2 = request.GET.get("long_2", None)
	lat_3 = request.GET.get("lat_3", None)
	long_3 = request.GET.get("long_3", None)
	lat_4 = request.GET.get("lat_4", None)
	long_4 = request.GET.get("long_4", None)
	lat_5 = request.GET.get("lat_5", None)
	long_5 = request.GET.get("long_5", None)
	lat_6 = request.GET.get("lat_6", None)
	long_6 = request.GET.get("long_6", None)
	lat_7 = request.GET.get("lat_7", None)
	long_7 = request.GET.get("long_7", None)
	lat_8 = request.GET.get("lat_8", None)
	long_8 = request.GET.get("long_8", None)

	lat_long_pairs = [
    (lat_1, long_1),
    (lat_2, long_2),
    (lat_3, long_3),
    (lat_4, long_4),
    (lat_5, long_5),
    (lat_6, long_6),
    (lat_7, long_7),
    (lat_8, long_8)
	]

	name_addresses = coordinate_converter(*lat_long_pairs)


	if lat_1 and lat_2:
		directions = Directions(
			lat_1= lat_1,
			long_1=long_1,
			lat_2 = lat_2,
			long_2=long_2,
			lat_3= lat_3,
			long_3=long_3,
			lat_4= lat_4,
			long_4=long_4,
			lat_5=lat_5,
			long_5=long_5,
			lat_6 = lat_6,
			long_6=long_6,
			lat_7= lat_7,
			long_7=long_7,
			long_8=long_8,
			lat_8=lat_8,
			)
		
	stops = directions["stops"]
	stop_number = []
	i = 0
	while i < stops:
		stop_number.append(i+1)
		i+=1

			
	stop_google_id = ["id-google-address-3", "id-google-address-4", "id-google-address-5", "id-google-address-6", "id-google-address-7", "id-google-address-8"]
	stop_name = ["stop1_address", "stop2_address", "stop3_address", "stop4_address", "stop5_address", "stop6_address"]
	stop_spec = ["stop1_spec", "stop2_spec", "stop3_spec", "stop4_spec", "stop5_spec", "stop6_spec"]
	stop_notes = ["stop1_notes", "stop2_notes", "stop3_notes", "stop4_notes", "stop5_notes", "stop6_notes"]
	stop_value = [name_addresses[2], name_addresses[3], name_addresses[4], name_addresses[5], name_addresses[6]]
	j = 0

	while j < stops:
		del stop_google_id[stops:]
		del stop_name[stops:]
		del stop_spec[stops:]
		del stop_value[stops:]
		del stop_notes[stops:]
		j+=1


	stop_info = zip(stop_number, stop_google_id, stop_name, stop_spec, stop_notes, stop_value)	


	submitted = False
	if request.method == "POST":
		form = NoticeOrderForm(request.POST)

		if form.is_valid():
			form.save()
			orderId = form.cleaned_data.get('order_id')
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			pickup_address = form.cleaned_data['pickup_address']
			pickup_spec = form.cleaned_data['pickup_spec']
			pickup_notes = form.cleaned_data['pickup_notes']
			stop1_address = form.cleaned_data.get('stop1_address')
			stop1_spec = form.cleaned_data.get('stop1_spec')
			stop1_notes = form.cleaned_data.get('stop1_notes')
			stop2_address = form.cleaned_data.get('stop2_address')
			stop2_spec = form.cleaned_data.get('stop2_spec')
			stop2_notes = form.cleaned_data.get('stop2_notes')
			stop3_address = form.cleaned_data.get('stop3_address')
			stop3_spec = form.cleaned_data.get('stop3_spec')
			stop3_notes = form.cleaned_data.get('stop3_notes')
			stop4_address = form.cleaned_data.get('stop4_address')
			stop4_spec = form.cleaned_data.get('stop4_spec')
			stop4_notes = form.cleaned_data.get('stop4_notes')
			stop5_address = form.cleaned_data.get('stop5_address')
			stop5_spec = form.cleaned_data.get('stop5_spec')
			stop5_notes = form.cleaned_data.get('stop5_notes')
			stop6_address = form.cleaned_data.get('stop6_address')
			stop6_spec = form.cleaned_data.get('stop6_spec')
			stop6_notes = form.cleaned_data.get('stop6_notes')
			dropoff_address = form.cleaned_data['dropoff_address']
			dropoff_spec = form.cleaned_data['dropoff_spec']
			dropoff_notes = form.cleaned_data['dropoff_notes']
			contact_number = form.cleaned_data['contact']
			delivery_type  = form.cleaned_data['delivery_type']
			delivery_date = form.cleaned_data['delivery_date']
			delivery_time = form.cleaned_data['delivery_time']
			flyer = form.cleaned_data['flyer']
			standard_fee = form.cleaned_data['standard_fee']
			priority_fee = form.cleaned_data['priority_fee']
			
			stop_spec_list = []
			stop_notes_list = []
			if stop1_address:
				stop_spec_list.append(stop1_spec)
				stop_notes_list.append(stop1_notes)
				if stop2_address:
					stop_spec_list.append(stop2_spec)
					stop_notes_list.append(stop2_notes)
					if stop3_address:
						stop_spec_list.append(stop3_spec)
						stop_notes_list.append(stop3_notes)
						if stop4_address:
							stop_spec_list.append(stop4_spec)
							stop_notes_list.append(stop4_notes)
							if stop5_address:
								stop_spec_list.append(stop5_spec)
								stop_notes_list.append(stop5_notes)
								if stop6_address:
									stop_spec_list.append(stop6_spec)
									stop_notes_list.append(stop6_notes)
				


			message = f'Hi there {name}, \n\nThank you for choosing CourtRun Legal Couriers to deliver your documents.'
			message += f'\n\nPickup Address: {pickup_address} \n\nPickup Address Specifications: {pickup_spec} \n\nPickup Notes: {pickup_notes}' 

			for i in range(stops):
				message += f'\n\n\nRespondent{i+1} Address: {stop_value[i]} \n\nRespondent{i+1} Address Specifications: {stop_spec_list[i]} \n\nRespondent{i+1} Notes: {stop_notes_list[i]}'

			message += f'\n\n\nDrop-off Address: {dropoff_address} \n\nDrop Address Specifications: {dropoff_spec} \n\nDrop-off Notes: {dropoff_notes}' 
			message += f'\n\n\nContact Number: {contact_number} \n\nDelivery Type: {delivery_type}'
			message += f'\nScheduled Delivery Date: {delivery_date} \nScheduled Delivery Time: {delivery_time}'
			message += f'\n\nProtective & Confidential Sleeve: {flyer}'
			message += f'\n\n\nThe email containing the payment link will provide a detailed breakdown of the total price.'
			message += f'\n\nWarm Regards,\nCourtRun Sales Team.'

			send_mail(subject=f'CourtRun Notice Order Confirmation #{orderId}',
					message=message,
					from_email=settings.EMAIL_HOST_USER,
					recipient_list=[email]
					)


			messageAdmin = f'Hi there {name}, \n\nThank you for choosing CourtRun Legal Couriers to deliver your documents.'
			messageAdmin += f'\n\nPickup Address: {pickup_address} \n\nPickup Address Specifications: {pickup_spec} \n\nPickup Notes: {pickup_notes}' 
			
			for i in range(stops):
				message += f'\n\n\nRespondent{i+1} Address: {stop_value[i]} \n\nRespondent{i+1} Address Specifications: {stop_spec_list[i]} \n\nRespondent{i+1} Notes: {stop_notes_list[i]}'			
			
			messageAdmin += f'\n\n\nDrop-off Address: {dropoff_address} \n\nDrop Address Specifications: {dropoff_spec} \n\nDrop-off Notes: {dropoff_notes}' 
			messageAdmin += f'\n\n\nContact Number: {contact_number} \n\nDelivery Type: {delivery_type}'
			messageAdmin += f'\nScheduled Delivery Date: {delivery_date} \nScheduled Delivery Time: {delivery_time}'
			messageAdmin += f'\n\nProtective & Confidential Sleeve: {flyer}'
			messageAdmin += f'\n\n\n\n\n==FEES FROM ORDER =='
			messageAdmin += f'\n\nStandard fee: {standard_fee}'
			messageAdmin += f'\nPriority fee: {priority_fee}'

			send_mail(subject=f'CourtRun Notice Order Confirmation #{orderId}',
					message=messageAdmin,
					from_email=settings.EMAIL_HOST_USER,
					recipient_list=['courtrun.orders@zektechnologies.co.za']
					)

			return HttpResponseRedirect('confirmation/')
		else:
			form = NoticeOrderForm
			if 'submitted' in request.GET:
				submitted = True

	form = NoticeOrderForm


	context = {
	"google_api_key": settings.GOOGLE_API_KEY,
	"lat_1": lat_1,
	"long_1": long_1,
	'name_1': name_addresses[0],
	"lat_2": lat_2,
	"long_2": long_2,
	"name_2": name_addresses[1],
	"lat_3": lat_3,
	"long_3": long_3,
	"lat_4": lat_4,
	"long_4": long_4,
	"lat_5": lat_5,
	"long_5": long_5,
	"lat_6": lat_6,
	"long_6": long_6,
	"lat_7": lat_7,
	"long_7": long_7,
	"lat_8": lat_8,
	"long_8": long_8,
	"stop_info": stop_info,
	"origin": f'{lat_1}, {long_1}',
	"destination": f'{lat_2}, {long_2}',
	"directions": directions,
	"form": form,
	"submitted": submitted,
	"Priority_Fee": float(directions["priority_fee"]) + (15 * stops), 
	"Standard_Fee": float(directions["standard_fee"]) + (15 * stops), 

	}
	return render(request, 'main/map-notice.html', context)


def confirmation(request):
	return render(request, 'main/confirmation.html')


def pricing(request):
	return render(request, 'main/pricing.html')


def page_not_found(request):
	return render(request, 'main/page-not-found.html')


def popia(request):
	return render(request, 'main/popia.html')


def privacy_policy(request):
	return render(request, 'main/privacy-policy.html')


def terms_and_conditions(request):
	return render(request, 'main/terms-and-conditions.html')


def faq(request):
	return render(request, 'main/faq.html')


def contact(request):
	submitted = False
	if request.method == "POST":
		form = ContactForm(request.POST)

		if form.is_valid():
			form.save()
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			number = form.cleaned_data['number']
			message = form.cleaned_data['message']


			send_mail(subject = f'CourtRun, {name} sent a message',
			message = f'{message} \n\n\nContact Phone number: {number}',
			from_email = {email},
			recipient_list = ['courtrun.contact@zektechnologies.co.za'],
			)

			return HttpResponseRedirect('/')
		else:
			form = ContactForm
			if 'submitted' in request.GET:
				submitted = True


	context = {
		'form': form
	}

	return render(request, 'main/contact.html', context)


def coordinate_converter(*coordinates):

	results = []
	for lat, long in coordinates:
		try:
			name = geolocator.reverse(f'{lat}, {long}')
			results.append(name.address)
		except ValueError:
			results.append("Location not specified")
	return tuple(results)