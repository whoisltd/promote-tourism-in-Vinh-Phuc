function iconLocation(feature, latlng) {
    var icontype = ""
    if(feature.typeFeature == 'Service'){
        icontype = "services-icon"
    }
    else if(feature.typeFeature == 'Place'){
        icontype = "place-icon"
    }
    else if(feature.typeFeature == 'Area'){
        icontype = "area-icon"
    }
    var iconCus = L.icon({
        iconUrl: "../../static/images/icons/" + icontype + ".png",
        iconSize: [35, 35],
        iconAnchor: [12, 41],
        popupAnchor: [5, -34],
        shadowSize: [41, 41]
    })
    return L.marker(latlng, { icon: iconCus })
}

//     $.get('https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat=47.217954&lon=-1.552918', function(data){
//     console.log(data.address.road);
// });

//function for direction
function choosePoint(name, num1, num2){
    $(name).click(function(){
        var a = parseFloat($(this).attr('data-lat'));
        var b = parseFloat($(this).attr('data-lng'));
        var c = [a, b];
        control.spliceWaypoints(num1, num2, c);
    })
}

//Features
function placeFeature(feature, layer) {
    feature.layer = layer;
    if (feature.properties) {
        layer.bindPopup("<b>Tên địa danh: </b>" + feature.properties.name + "<br>"
        + "<b>Hình ảnh: </b>" + "<img src='static/" + feature.properties.image + "' width='100px' height='100px'>" + "<br>"
        + '<button class="thisIsStartPoint" data-lat="'+ feature.geometry.coordinates[1] +'" data-lng="'+ feature.geometry.coordinates[0]+'">Use this as start point</button>' + "<br>"
        + '<button class="thisIsEndPoint" data-lat="'+ feature.geometry.coordinates[1] +'" data-lng="'+ feature.geometry.coordinates[0]+'">Use this as end point</button>' + "<br>"
        ).on("popupopen", function() {
            choosePoint('.thisIsStartPoint', 0, 1);
            choosePoint('.thisIsEndPoint', 1, 1);

        })

    }
}

function areaFeature(feature, layer) {
    feature.layer = layer;
    if (feature.properties) {
        layer.bindPopup("<b>Khu du lịch: </b>" + feature.properties.name + "<br>"
        + '<button class="thisIsStartPoint" data-lat="'+ feature.geometry.coordinates[1] +'" data-lng="'+ feature.geometry.coordinates[0]+'">Use this as start point</button>' + "<br>"
        + '<button class="thisIsEndPoint" data-lat="'+ feature.geometry.coordinates[1] +'" data-lng="'+ feature.geometry.coordinates[0]+'">Use this as end point</button>' + "<br>"
        ).on("popupopen", function() {
            choosePoint('.thisIsStartPoint', 0, 1);
            choosePoint('.thisIsEndPoint', 1, 1);
        })
    }
}

function serviceFeature(feature, layer) {
    feature.layer = layer;
    if (feature.properties) {
        layer.bindPopup("<b>Loại dịch vụ: </b>" + feature.properties.type + "<br>"
        + "<b>Tên: </b>" + feature.properties.name + "<br>"
        + "<b>Địa chỉ: </b>" + feature.properties.address + "<br>"
        + "<b>Số điện thoại: </b>" + feature.properties.phone + "<br>"
        + "<b>Email: </b>" + feature.properties.email + "<br>"
        + "<b>Hình ảnh: </b>" + "<img src='static/" + feature.properties.image + "' width='100px' height='100px'>" + "<br>"
        + '<button class="thisIsStartPoint" data-lat="'+ feature.geometry.coordinates[1] +'" data-lng="'+ feature.geometry.coordinates[0]+'">Use this as start point</button>' + "<br>"
        + '<button class="thisIsEndPoint" data-lat="'+ feature.geometry.coordinates[1] +'" data-lng="'+ feature.geometry.coordinates[0]+'">Use this as end point</button>' + "<br>"

        + "<a>Xem thêm</a>" + "<br>"
        ).on("popupopen", function() {
            choosePoint('.thisIsStartPoint', 0, 1);
            choosePoint('.thisIsEndPoint', 1, 1);
        })

    }
}


//Layer Group
var markersLayer = new L.LayerGroup();

// Get API
function getAPI(link) {
    var overlay = null;
    $.ajax({
        type: "GET",
        datatype: "JSON",
        url: link,
        async: !1,
        success: function (response) {
            console.log(response)
            if (link == "/api/v1/places") {
                overlay = L.geoJSON(response, {
                    pointToLayer: iconLocation, onEachFeature: placeFeature
                })
                markersLayer.addLayer(overlay)
            }
            else if (link == "/api/v1/areas") {
                overlay = L.geoJSON(response, {
                    pointToLayer: iconLocation, onEachFeature: areaFeature
                })
                markersLayer.addLayer(overlay)
            }
            else if (link == "/api/v1/services") {
                overlay = L.geoJSON(response, {
                    pointToLayer: iconLocation, onEachFeature: serviceFeature
                })
                markersLayer.addLayer(overlay)
            }
        }
    })
    return overlay
}

//layer places, areas, services
var place = getAPI("/api/v1/places")
var area = getAPI("/api/v1/areas")
var service = getAPI("/api/v1/services")

//add layer to map
map.addLayer(markersLayer)

// Control layers
var baseLayers = {
    "Open Street Maps": osm
}
var overlays = {
    "Place": place,
    "Area": area,
    "Service": service
}

L.control.layers(baseLayers, overlays).addTo(map)

//map legend
var legend = L.control({ position: 'bottomright' })
legend.onAdd = function (map) {
    var div = L.DomUtil.create('div', 'info')
    div.innerHTML += '<img style="width:30px;height:30px" src="../../static/images/icons/place-icon.png">: Place<br>'
    div.innerHTML += '<img style="width:30px;height:30px" src="../../static/images/icons/services-icon.png">: Service<br>'
    div.innerHTML += '<img style="width:30px;height:30px" src="../../static/images/icons/area-icon.png">: Area<br>'
    return div
}
legend.addTo(map)