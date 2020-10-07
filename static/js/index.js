$(function(){
    $("#checkbox").click(function () {
        $.ajax({
            type: "GET",
            url: "ajax_form/",
            data: {
                'checkbox': $("#checkbox").val(),
            },
            dataType: "text",
            cache: false,
            success: function (data) {
                if (data == 'ON') {
                    $(".buttonForChange").prop('disabled', false);
                }
                else if (data == 'OFF'){
                    $(".buttonForChange").prop('disabled', true);
                }
            }
        });
    });
});
