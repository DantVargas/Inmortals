function iniciarMap(){
    var coord = {lat:-33.0089245 ,lng: -71.5482706};
    var map = new google.maps.Map(document.getElementById('map'),{
      zoom: 50,
      center: coord
    });
    var marker = new google.maps.Marker({
      position: coord,
      map: map
    });
}