//draw Item
drawnItems = L.featureGroup().addTo(map);
map.addControl(new L.Control.Draw({
    edit: {
        featureGroup: drawnItems,
        poly: {
            allowIntersection: false
        }
    },
    draw: {
        polygon: false,
        circle: false,
        polyline: false,
        rectangle: false,
        circlemarker: false

    }
}));

// Truncate value based on number of decimals
var _round = function(num, len) {
    return Math.round(num*(Math.pow(10, len)))/(Math.pow(10, len));
};
// Helper method to format LatLng object (x.xxxxxx, y.yyyyyy)
var strLatLng = function(latlng) {
    return _round(latlng.lat, 6)+", "+_round(latlng.lng, 6);
};

var getPopupContent = function(layer) {
    // Marker - add lat/long
    return strLatLng(layer.getLatLng());
};

map.on(L.Draw.Event.CREATED, function(event) {
    var layer = event.layer;
    var content = getPopupContent(layer)+'<br><input type="checkbox" id="checkService" name="check" value="Service">'
    +'<label for="checkService">Service</label><br>'
    +'<input type="checkbox" id="checkArea" name="check" value="Area">'
    +'<label for="checkArea">Area</label><br>'
    +'<input type="checkbox" id="checkPlace" name="check" value="Place">'
    +'<label for="checkPlace">Place</label><br>'
    +'<button id="save">Save</button>';
    if (content !== null) {
        layer.bindPopup(content).on("popupopen", function() {
            $("input:checkbox").on('click', function() {
            var $box = $(this);
            console.log($box.val())
            if ($box.is(":checked")) {
                var group = "input:checkbox[name='" + $box.attr("name") + "']";
                console.log(group)
                $(group).prop("checked", false);
                $box.prop("checked", true);
            } else {
                $box.prop("checked", false);
            }});

            $("#save").click(function(){
                var check = $("input:checkbox:checked").val()
                function toDb(type){
                    console.log(type)
                    var lattt = layer.getLatLng()
                    console.log(lattt)
                    var geoJSON = {
                        "typeMarker": type,
                        "geometry": {
                            "type": "Point",
                            "coordinates": [lattt['lng'], lattt['lat']]
                        },
                    }
                    $.ajax({
                            url: "/createNewItem",
                            type: "POST",
                            contentType: "application/json",
                            data: JSON.stringify(geoJSON),
                            success: function (data) { }
                    });
                }
                if (check == "Service"){
                    var geoJSON = toDb("Service")
                }
                else if (check == "Area"){
                    var geoJSON = toDb("Area")
                }
                else if (check == "Place"){
                    var geoJSON = toDb("Place")
                }
            })
    });
    }
    drawnItems.addLayer(layer);
});
