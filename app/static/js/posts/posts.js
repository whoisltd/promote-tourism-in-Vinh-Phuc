//function get data to items
function get_data(link){
    var areas=[];
    areas = $.map($(".areas"),function(select){
        if ($(select).prop('checked')) {
            return $(select).attr("value");
        }
    });
    req = $.ajax({
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify({'areas':areas}),
        type: 'POST',
        url: link
    });
    req.done(function (data) {
        console.log(data);
        $('#testttt').html(data);
    });
}

// pagination
$(document).ready(function () {

    $(document).on('click', '.page-link', function (event) {
        var link = $(this).attr('href');
        get_data(link);
        event.preventDefault();
    });
});

//areas
$('.areas').click(function () {
    if ($(this).prop('checked')) {
        get_data('/posts1');
    } else {
        get_data('/posts1');
    }
})

