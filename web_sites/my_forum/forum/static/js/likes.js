$(document).ready(function() {
     var btn_inp = [];
    $("a[name='like']").on('click',
            function (event) {
                event.preventDefault();
                btn_inp = [
                {   name: 'csrfmiddlewaretoken',
                    value: csrftoken
                },
                {
                    name: event.target.title,
                    value: event.target.id
                }
            ];
            $.ajax({
            type: "POST",
            url: window.location.href,
            data: btn_inp
            }).done(function (data) {
                if (data.done != undefined) {
                    $("#"+ event.target.id).append("<span class='label label-primary'>" + data.done + "</span>");
                } else if (data.delete != undefined) {
                     $("#"+ event.target.id + " span:contains(" + data.delete + ")").remove();
                }});
            });

});
