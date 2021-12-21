//Current location
mylocation = L.control.locate({
    position: 'topleft',
    strings: {
        title: "My location",
        popup: 'You are here<br><button id="useToStart">use this as start point</button><br><button id="useToEnd">use this as end point</button>',
    },
}).addTo(map);

//get current location 
var myloca
map.on('locationfound', function (self) {
myloca = [self.latlng.lat, self.latlng.lng]
});

//use for directions
map.on('popupopen', function (self) {
    $('#useToStart').click(function () {
        control.spliceWaypoints(0, 1, myloca);
    });

    $('#useToEnd').click(function () {
        control.spliceWaypoints(1, 1, myloca);
    });
});