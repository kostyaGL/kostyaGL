submitLike = function (event) {
    $("a[name='like']").on('click',
        function () {
            event.preventDefault();
            var btn_inp = [
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
                    console.log(data.delete);
                     $("#"+ event.target.id + " span:contains(" + data.delete + ")").remove();
                }
            });
        });
};