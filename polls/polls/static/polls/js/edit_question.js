$('#myEditModal').on('shown.bs.modal',
        function () {
            $('#myInput').focus()
        });

submitEditForm = function(event){
event.preventDefault();
var $error_message = $('#error');
var obj = JSON.parse(JSON.stringify($('#edit_question_form').serializeArray()));
$.ajax({
    type: "POST",
    url: "/edit_question/",
    data: obj
}).done(function(data){
    if (data=='delete') {
        setTimeout(function(){window.location.replace("/")}, 500);
           } else if (data == 'delete'){
        $error_message.show();
    }
        });
};