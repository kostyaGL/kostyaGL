submitLike = function (event) {
    $("a[name='like']").on('click',
        function () {
            console.log(event);
            event.preventDefault();
            var id_btn = event.target.id;
            var name = event.target.title;
            var btn_inp = [{name: 'csrfmiddlewaretoken', value: csrftoken}, {name: name, value: id_btn}];
            $.ajax({
                type: "POST",
                url: window.location.href,
                data: btn_inp
            }).done(function (data) {
                if (data == 'done') {
                    setTimeout(function () {
                        window.location.replace(window.location.href)
                    }, 500);
                } else if (data == 'undo') {
                    console.log(id_btn);
                }

            });

        });
};