submitLike = function(event){
event.preventDefault();
var $error_message = $('#error');
var obj = JSON.parse(JSON.stringify($('#likes_form').serializeArray()));
    console.log("url " + window.location.href);
$.ajax({
    type: "POST",
    url: "/1/posts/",
    data: obj
}).done(function(data){
    if (data=='delete') {
        setTimeout(function(){window.location.replace("/")}, 500);
           } else if (data == 'delete'){
        $error_message.show();
    }
        });
};