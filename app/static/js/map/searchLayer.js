 //search
var selector = L.control({
    position: 'topright'
});

selector.onAdd = function(map) {
    var div = L.DomUtil.create('div', 'mySelector');
    div.innerHTML = '<input id = "opt" type="text" list="marker_select" /><datalist id="marker_select"><option value="init"></option></datalist>';
    return div;
};
selector.addTo(map);

var markers = markersLayer.getLayers();
// console.log(markers)
function markerLayer(i){
    markers[i].eachLayer(function(layer) {
        var optionElement = document.createElement("option");
        optionElement.setAttribute("data-value", layer._leaflet_id);
        optionElement.value = layer.feature.properties.name;
        L.DomUtil.get("marker_select").appendChild(optionElement);
    });
    var marker_select = L.DomUtil.get("opt");
    L.DomEvent.addListener(marker_select, 'click', function(e) {
        L.DomEvent.stopPropagation(e);
    });

    L.DomEvent.addListener(marker_select, 'change', changeHandler);

    function changeHandler(e) {
        var valOption = $('option[value="'+e.target.value+'"]').data('value');
        if (e.target.value == "init") {
            map.closePopup();
        } else {
            markers[i].getLayer(valOption).openPopup();
        }
    }
}
for (var i = 0; i < markers.length; i++) {
    markerLayer(i);
}