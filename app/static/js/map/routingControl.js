//Routing control
var control = L.Routing.control({
    router: L.Routing.osrmv1({
        liveTraffic: true,
        profile: 'Driving',
    }),
    geocoder: L.Control.Geocoder.nominatim(),
    routeWhileDragging: true,
    reverseWaypoints: true
    })

L.easyButton('fa-level-up',
    function() {  
        if (control._map) {
            map.removeControl(control)
        }
        else {
            map.addControl(control)
        }
    }
).addTo(map);