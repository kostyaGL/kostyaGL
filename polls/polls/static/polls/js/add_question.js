$('#myModal').on('shown.bs.modal',
        function () {
            $('#myInput').focus()
        });

var $input = $('#number');
var $modal_body = $('#adder');
var $to_append = '<p></p><input id="choices_text" type="text" name="choices_text" value="">';
$('[id^=agr_btn]').on('click', function () {
    var $choices = $('[id^=choices_text]');
    if ($(this).hasClass('btn btn-white btn-minus')) {
        var $parsed = parseInt($input.val());
        if (($parsed - 1) < 1) {
            }
            else {
                $input.val($parsed - 1);
                $choices[$parsed - 1].remove();
        }
    } else {
        $input.val(parseInt($input.val()) + 1);
        $modal_body.append($to_append);
    }
});

submitForm = function(event){
event.preventDefault();
var $error_message = $('#error');
var obj = JSON.parse(JSON.stringify($('#question_form').serializeArray()));
$.ajax({
    type: "POST",
    url: "/add_question/",
    data: obj
}).done(function(data){
    if (data=='saved') {
        setTimeout(function(){window.location.replace("/")}, 500);
           } else if (data == 'fuck'){
        $error_message.show();
    }
        });
};
