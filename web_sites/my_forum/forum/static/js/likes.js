submitLike = function (event) {
    $("a[name='like']").on('click',
        function () {
            console.log(event);
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
                if (data == 'done') {
                    setTimeout(function () {
                        window.location.replace(window.location.href)
                    });
                } else if (data == 'undo') {
                }
            });
        });
};