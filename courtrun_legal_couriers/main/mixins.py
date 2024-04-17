from django.conf import settings
import requests
from humanfriendly import format_timespan


'''
Handles directions from Google
'''

def Directions(*args, **kwargs):
	
	
	lat_1 = kwargs.get("lat_1", None)
	long_1 = kwargs.get("long_1", None)
	lat_2 = kwargs.get("lat_2", None)
	long_2 = kwargs.get("long_2", None)
	lat_3 = kwargs.get("lat_3", None)
	long_3 = kwargs.get("long_3", None)
	lat_4 = kwargs.get("lat_4", None)
	long_4 = kwargs.get("long_4", None)
	lat_5 = kwargs.get("lat_5", None)
	long_5 = kwargs.get("long_5", None)
	lat_6 = kwargs.get("lat_6", None)
	long_6 = kwargs.get("long_6", None)
	lat_7 = kwargs.get("lat_7", None)
	long_7 = kwargs.get("long_7", None)
	lat_8 = kwargs.get("lat_8", None)
	long_8 = kwargs.get("long_8", None)
	stops = 0


	origin = f'{lat_1},{long_1}'
	destination = f'{lat_2},{long_2}'
	if lat_3 == "undefined":
		waypoints = f''
	else:
		waypoints = f'{lat_3},{long_3}'
		stops+=1
		if lat_4 != "undefined":
			waypoints+=f"|{lat_4},{long_4}"
			stops+=1
			if lat_5 != "undefined":
				waypoints+=f"|{lat_5},{long_5}"
				stops+=1
				if lat_6 != "undefined":
					waypoints+=f"|{lat_6},{long_6}"
					stops+=1
					if lat_7 != "undefined":
						waypoints+=f"|{lat_7},{long_7}"
						stops+=1
						if lat_8 != "undefined":
							waypoints+=f"|{lat_8},{long_8}"
							stops+=1


	
	result = requests.get(
		'https://maps.googleapis.com/maps/api/directions/json?',
		params={
		'origin': origin,
		'destination': destination,
		'waypoints': waypoints,
		"key": settings.GOOGLE_API_KEY
		})



	directions = result.json()

	if directions["status"] == "OK":

		routes = directions["routes"][0]["legs"]
		distance = 0
		duration = 0
		route_list = []

		for route in range(len(routes)):

			distance += int(routes[route]["distance"]["value"])
			duration += int(routes[route]["duration"]["value"])

			route_step = {
				'origin': routes[route]["start_address"],
				'destination': routes[route]["end_address"],
				'distance': routes[route]["distance"]["text"],
				'duration': routes[route]["duration"]["text"],

				'steps': [
					[
						s["distance"]["text"],
						s["duration"]["text"],
						s["html_instructions"],

					]
					for s in routes[route]["steps"]]
				}

			
			route_list.append(route_step)


		distanceValue = float(round(distance/1000, 2))
		bag_fee = 25

		#Standard Fee calculation
		if distanceValue > 0:
			total_distance = distanceValue
			if total_distance > 30:
				in_radius=30 * 4.5
				total_distance-=30
				out_of_radius = total_distance * 5.5
				standard_fee = in_radius + out_of_radius + bag_fee
			else:
				standard_fee = total_distance * 4.5 + bag_fee


		#Priority Fee calculation
		if distanceValue > 0:
			total_distance = distanceValue
			if total_distance > 30:
				in_radius=30 * 6.5
				total_distance-=30
				out_of_radius = total_distance * 7.5
				priority_fee = in_radius + out_of_radius + bag_fee
			else:
				priority_fee = total_distance * 6.5 + bag_fee
		
		
	return {
		"origin": origin,
		"destination": destination,
		"distance": f"{round(distance/1000, 2)} Km",
		"duration": format_timespan(duration),
		"route": route_list,
		"standard_fee": format(standard_fee,".2f"),
		"priority_fee": format(priority_fee, ".2f"),
		"stops": stops
		}
