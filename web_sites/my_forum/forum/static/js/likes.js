submitLike = function(event){
event.preventDefault();
var $error_message = $('#error');
var obj = JSON.parse(JSON.stringify($('#likes_form').serializeArray()));
$.ajax({
    type: "POST",
    url: window.location.pathname,
    data: obj
}).done(function(data){
    if (data=='done') {
        setTimeout(function(){window.location.replace("/")}, 500);
           } else if (data == 'delete'){
        $error_message.show();
    }
        });
};