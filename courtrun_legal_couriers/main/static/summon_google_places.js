
$.getScript( "https://maps.googleapis.com/maps/api/js?key=" + google_api_key + "&libraries=places") 
.done(function( script, textStatus ) {
    google.maps.event.addDomListener(window, "load", initAutocomplete())

})


var auto_fields = [1, 2, 3, 4, 5, 6, 7, 8]

function initAutocomplete() {

    for (i = 0; i < auto_fields.length; i++) {
        var field = auto_fields[i]
        window['autocomplete_'+field] = new google.maps.places.Autocomplete(
          document.getElementById('id-google-address-' + field),
        {
           types: ['establishment'],
           componentRestrictions: {'country': ['za']},
        })
      }



  autocomplete_1.addListener('place_changed', function(){
    onPlaceChanged('1')
  });

  
  autocomplete_2.addListener('place_changed', function(){
    onPlaceChanged('2')
  });

  autocomplete_3.addListener('place_changed', function(){
    onPlaceChanged('3')
  });

  
  autocomplete_4.addListener('place_changed', function(){
    onPlaceChanged('4')
  });

  autocomplete_5.addListener('place_changed', function(){
    onPlaceChanged('5')
  });

  
  autocomplete_6.addListener('place_changed', function(){
    onPlaceChanged('6')
  });

  autocomplete_7.addListener('place_changed', function(){
    onPlaceChanged('7')
  });

  
  autocomplete_8.addListener('place_changed', function(){
    onPlaceChanged('8')
  });


}


function onPlaceChanged (addy){

    var auto = window['autocomplete_'+addy]
    var el_id = 'id-google-address-'+addy
    var lat_id = 'id-lat-' + addy
    var long_id = 'id-long-' + addy

    var geocoder = new google.maps.Geocoder()
    var address = document.getElementById(el_id).value

    geocoder.geocode( { 'address': address}, function(results, status) {

        if (status == google.maps.GeocoderStatus.OK) {
            var latitude = results[0].geometry.location.lat();
            var longitude = results[0].geometry.location.lng();

            $('#' + lat_id).val(latitude) 
            $('#' + long_id).val(longitude) 

            CalcRoute()
        } 
    }); 
}


function validateForm() {
    var valid = true;
    $('.geo').each(function () {
        if ($(this).val() === '') {
            valid = false;
            return false;
        }
    });
    return valid
}


function CalcRoute(){

    if ( validateForm() == true){

        var latname = []
        var longname = []
        var latval = []
        var longval =[]
        var latcoords = {}
        var longcoords = {}

        
        for (i = 0; i < auto_fields.length; i++){
            var field = auto_fields[i]
            latvar_id = 'lat_'+field
            longvar_id = 'long_'+field
            latval_id = $('#id-lat-' + field).val()
            longval_id = $('#id-long-' + field).val()

            latname.push(latvar_id)
            longname.push(longvar_id)
            latval.push(latval_id)
            longval.push(longval_id)
        }

        for (i = 0; i < latname.length; i++){
            latcoords[latname[i]] = latval[i]
            longcoords[longname[i]] = longval[i]
        }

        var params = Object.assign({}, latcoords, longcoords);


      var esc = encodeURIComponent;
      var query = Object.keys(params)
          .map(k => esc(k) + '=' + esc(params[k]))
          .join('&');

      url = '/summon-order-details?' + query
      window.location.assign(url)
    }
}