
$.getScript( "https://maps.googleapis.com/maps/api/js?key=" + google_api_key + "&libraries=places") 
.done(function( script, textStatus ) {
    google.maps.event.addDomListener(window, "load", initMap)

})

function initMap() {
    var directionsService = new google.maps.DirectionsService;
    var directionsDisplay = new google.maps.DirectionsRenderer;
    var map = new google.maps.Map(document.getElementById('map-route'), {
        zoom: 7,
        center: {lat: lat_1, lng: long_1}
    });

    directionsDisplay.setMap(map);
    calculateAndDisplayRoute(directionsService, directionsDisplay);
}


var waypts = [];

if (typeof lat_3 !== "undefined" && typeof long_3 !== "undefined") {
  waypts.push({
      location: {lat: lat_3, lng: long_3},
      stopover: true
  });
}

if (typeof lat_4 !== "undefined" && typeof long_4 !== "undefined") {
  waypts.push({
      location: {lat: lat_4, lng: long_4},
      stopover: true
  });
}

if (typeof lat_5 !== "undefined" && typeof long_5 !== "undefined") {
  waypts.push({
      location: {lat: lat_5, lng: long_5},
      stopover: true
  });
}

if (typeof lat_6 !== "undefined" && typeof long_6 !== "undefined") {
  waypts.push({
      location: {lat: lat_6, lng: long_6},
      stopover: true
  });
}

if (typeof lat_7 !== "undefined" && typeof long_7 !== "undefined") {
  waypts.push({
      location: {lat: lat_7, lng: long_7},
      stopover: true
  });
}

if (typeof lat_8 !== "undefined" && typeof long_8 !== "undefined") {
  waypts.push({
      location: {lat: lat_8, lng: long_8},
      stopover: true
  });
}

function calculateAndDisplayRoute(directionsService, directionsDisplay) {
    directionsService.route({
        origin: origin,
        destination: destination,
        waypoints: waypts,
        optimizeWaypoints: true,
        travelMode: google.maps.TravelMode.DRIVING,
    }, function(response, status) {
      if (status === 'OK') {
        directionsDisplay.setDirections(response);

      } else {
        alert('Directions request failed due to ' + status);
        window.location.assign("/route")
      }
    });
}